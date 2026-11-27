(() => {
  "use strict";

  const MIN_SCALE = 0.5;
  const MAX_SCALE = 6;
  const ZOOM_STEP = 1.25;
  const KEY_PAN_STEP = 48;
  const WHEEL_ZOOM_SENSITIVITY = 0.01;

  let activeObserver = null;
  let sharedDialog = null;
  let activeModalContext = null;

  function clamp(value, min, max) {
    return Math.min(max, Math.max(min, value));
  }

  function touchDistance(t1, t2) {
    return Math.hypot(t2.clientX - t1.clientX, t2.clientY - t1.clientY);
  }

  function touchMidpoint(t1, t2) {
    return {
      x: (t1.clientX + t2.clientX) / 2,
      y: (t1.clientY + t2.clientY) / 2,
    };
  }

  function createButton(action, label, text) {
    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = "diagram-pz__btn";
    btn.dataset.action = action;
    btn.setAttribute("aria-label", label);
    btn.textContent = text;
    return btn;
  }

  function ensureSharedDialog() {
    if (sharedDialog && sharedDialog.isConnected) {
      return sharedDialog;
    }
    const dialog = document.createElement("dialog");
    dialog.className = "diagram-pz__dialog";
    dialog.setAttribute("aria-label", "Expanded diagram");

    dialog.addEventListener("click", (event) => {
      if (event.target === dialog) {
        dialog.close();
      }
    });

    dialog.addEventListener("close", () => {
      if (!activeModalContext) {
        return;
      }
      const { placeholder, container, expandBtn, setFullscreen } = activeModalContext;
      activeModalContext = null;
      setFullscreen(false);
      if (placeholder.isConnected) {
        placeholder.replaceWith(container);
      }
      expandBtn.textContent = "Expand";
      expandBtn.setAttribute("aria-label", "Expand diagram fullscreen");
      expandBtn.focus();
    });

    document.body.appendChild(dialog);
    sharedDialog = dialog;
    return dialog;
  }

  function buildWrapper(mermaidEl) {
    const container = document.createElement("div");
    container.className = "diagram-pz";

    const toolbar = document.createElement("div");
    toolbar.className = "diagram-pz__toolbar";
    toolbar.setAttribute("role", "toolbar");
    toolbar.setAttribute("aria-label", "Diagram zoom controls");

    const zoomOutBtn = createButton("zoom-out", "Zoom out diagram", "−");
    const scaleLabel = document.createElement("span");
    scaleLabel.className = "diagram-pz__scale";
    scaleLabel.textContent = "100%";
    const zoomInBtn = createButton("zoom-in", "Zoom in diagram", "+");
    const resetBtn = createButton("reset", "Reset diagram view", "Reset");
    const expandBtn = createButton("fullscreen", "Expand diagram fullscreen", "Expand");

    toolbar.append(zoomOutBtn, scaleLabel, zoomInBtn, resetBtn, expandBtn);

    const viewport = document.createElement("div");
    viewport.className = "diagram-pz__viewport";
    viewport.tabIndex = 0;
    viewport.setAttribute("role", "group");
    viewport.setAttribute("aria-label", "Interactive diagram");

    const stage = document.createElement("div");
    stage.className = "diagram-pz__stage";

    mermaidEl.replaceWith(container);
    stage.appendChild(mermaidEl);
    viewport.appendChild(stage);
    container.append(toolbar, viewport);

    return { container, toolbar, viewport, stage, scaleLabel, expandBtn };
  }

  function attachPanZoom(mermaidEl) {
    if (!mermaidEl || mermaidEl.closest(".diagram-pz")) {
      return;
    }

    const { container, toolbar, viewport, stage, scaleLabel, expandBtn } =
      buildWrapper(mermaidEl);

    const state = {
      scale: 1,
      x: 0,
      y: 0,
      fullscreen: false,
    };

    let safariGestureActive = false;
    let safariGestureBaseScale = 1;
    let activeMousePointerId = null;
    let lastMousePos = null;
    let touchState = null;

    function isTransformed() {
      return (
        Math.abs(state.scale - 1) > 0.001 ||
        Math.abs(state.x) > 1 ||
        Math.abs(state.y) > 1
      );
    }

    function applyTransform() {
      stage.style.transform = `translate3d(${state.x}px, ${state.y}px, 0) scale(${state.scale})`;
      scaleLabel.textContent = `${Math.round(state.scale * 100)}%`;
      viewport.classList.toggle("is-zoomed", isTransformed());
    }

    function zoomAt(nextScale, clientX, clientY) {
      const clamped = clamp(nextScale, MIN_SCALE, MAX_SCALE);
      const rect = viewport.getBoundingClientRect();
      const px = clientX - rect.left;
      const py = clientY - rect.top;
      const ratio = clamped / state.scale;

      state.x = px - (px - state.x) * ratio;
      state.y = py - (py - state.y) * ratio;
      state.scale = clamped;
      applyTransform();
    }

    function zoomAroundCenter(factor) {
      const rect = viewport.getBoundingClientRect();
      zoomAt(
        state.scale * factor,
        rect.left + rect.width / 2,
        rect.top + rect.height / 2,
      );
    }

    function resetView() {
      state.scale = 1;
      state.x = 0;
      state.y = 0;
      applyTransform();
    }

    function toggleFullscreen() {
      const dialog = ensureSharedDialog();
      if (state.fullscreen && dialog.open) {
        dialog.close();
        return;
      }

      const placeholder = document.createElement("div");
      placeholder.className = "diagram-pz__placeholder";
      placeholder.style.minHeight = `${container.offsetHeight}px`;
      container.replaceWith(placeholder);

      state.fullscreen = true;
      container.classList.add("is-fullscreen");
      expandBtn.textContent = "Close";
      expandBtn.setAttribute("aria-label", "Close fullscreen diagram");

      activeModalContext = {
        placeholder,
        container,
        expandBtn,
        setFullscreen(value) {
          state.fullscreen = value;
          container.classList.toggle("is-fullscreen", value);
        },
      };

      dialog.appendChild(container);
      dialog.showModal();
      viewport.focus();
    }

    toolbar.addEventListener("click", (event) => {
      const btn = event.target.closest("button[data-action]");
      if (!btn) {
        return;
      }
      const action = btn.dataset.action;
      if (action === "zoom-in") {
        zoomAroundCenter(ZOOM_STEP);
      } else if (action === "zoom-out") {
        zoomAroundCenter(1 / ZOOM_STEP);
      } else if (action === "reset") {
        resetView();
      } else if (action === "fullscreen") {
        toggleFullscreen();
      }
    });

    viewport.addEventListener(
      "wheel",
      (event) => {
        if (event.ctrlKey || event.metaKey) {
          event.preventDefault();
          if (safariGestureActive) {
            return;
          }
          const factor = Math.exp(-event.deltaY * WHEEL_ZOOM_SENSITIVITY);
          zoomAt(state.scale * factor, event.clientX, event.clientY);
          return;
        }

        const isHorizontalPan = Math.abs(event.deltaX) > Math.abs(event.deltaY);
        if (state.fullscreen || isTransformed() || isHorizontalPan) {
          event.preventDefault();
          state.x -= event.deltaX;
          state.y -= event.deltaY;
          applyTransform();
        }
      },
      { passive: false },
    );

    viewport.addEventListener(
      "gesturestart",
      (event) => {
        event.preventDefault();
        safariGestureActive = true;
        safariGestureBaseScale = state.scale;
      },
      { passive: false },
    );

    viewport.addEventListener(
      "gesturechange",
      (event) => {
        event.preventDefault();
        if (!safariGestureActive) {
          return;
        }
        zoomAt(
          safariGestureBaseScale * event.scale,
          event.clientX,
          event.clientY,
        );
      },
      { passive: false },
    );

    viewport.addEventListener("gestureend", () => {
      safariGestureActive = false;
    });

    viewport.addEventListener("pointerdown", (event) => {
      if (event.pointerType !== "mouse" || event.button !== 0) {
        return;
      }
      activeMousePointerId = event.pointerId;
      lastMousePos = { x: event.clientX, y: event.clientY };
      viewport.classList.add("is-dragging");
      viewport.setPointerCapture(event.pointerId);
    });

    viewport.addEventListener("pointermove", (event) => {
      if (event.pointerId !== activeMousePointerId || !lastMousePos) {
        return;
      }
      state.x += event.clientX - lastMousePos.x;
      state.y += event.clientY - lastMousePos.y;
      lastMousePos = { x: event.clientX, y: event.clientY };
      applyTransform();
    });

    function endMouseDrag(event) {
      if (event.pointerId !== activeMousePointerId) {
        return;
      }
      activeMousePointerId = null;
      lastMousePos = null;
      viewport.classList.remove("is-dragging");
      if (viewport.hasPointerCapture(event.pointerId)) {
        viewport.releasePointerCapture(event.pointerId);
      }
    }

    viewport.addEventListener("pointerup", endMouseDrag);
    viewport.addEventListener("pointercancel", endMouseDrag);

    viewport.addEventListener("dblclick", (event) => {
      if (state.scale > 1.05) {
        resetView();
      } else {
        zoomAt(2, event.clientX, event.clientY);
      }
    });

    viewport.addEventListener(
      "touchstart",
      (event) => {
        if (event.touches.length === 2) {
          event.preventDefault();
          const [t1, t2] = event.touches;
          touchState = {
            mode: "pinch",
            dist: touchDistance(t1, t2),
            mid: touchMidpoint(t1, t2),
          };
        } else if (event.touches.length === 1 && (state.fullscreen || isTransformed())) {
          const t = event.touches[0];
          touchState = {
            mode: "pan",
            x: t.clientX,
            y: t.clientY,
          };
        } else {
          touchState = null;
        }
      },
      { passive: false },
    );

    viewport.addEventListener(
      "touchmove",
      (event) => {
        if (!touchState) {
          return;
        }
        if (event.touches.length === 2 && touchState.mode === "pinch") {
          event.preventDefault();
          const [t1, t2] = event.touches;
          const nextDist = touchDistance(t1, t2);
          const nextMid = touchMidpoint(t1, t2);

          state.x += nextMid.x - touchState.mid.x;
          state.y += nextMid.y - touchState.mid.y;

          if (touchState.dist > 0) {
            zoomAt(state.scale * (nextDist / touchState.dist), nextMid.x, nextMid.y);
          } else {
            applyTransform();
          }

          touchState.dist = nextDist;
          touchState.mid = nextMid;
        } else if (event.touches.length === 1 && touchState.mode === "pan") {
          event.preventDefault();
          const t = event.touches[0];
          state.x += t.clientX - touchState.x;
          state.y += t.clientY - touchState.y;
          touchState.x = t.clientX;
          touchState.y = t.clientY;
          applyTransform();
        }
      },
      { passive: false },
    );

    function resetTouchState(event) {
      if (event.touches.length === 2) {
        const [t1, t2] = event.touches;
        touchState = {
          mode: "pinch",
          dist: touchDistance(t1, t2),
          mid: touchMidpoint(t1, t2),
        };
      } else if (event.touches.length === 1 && (state.fullscreen || isTransformed())) {
        const t = event.touches[0];
        touchState = { mode: "pan", x: t.clientX, y: t.clientY };
      } else {
        touchState = null;
      }
    }

    viewport.addEventListener("touchend", resetTouchState);
    viewport.addEventListener("touchcancel", resetTouchState);

    viewport.addEventListener("keydown", (event) => {
      if (event.key === "+" || event.key === "=") {
        event.preventDefault();
        zoomAroundCenter(ZOOM_STEP);
      } else if (event.key === "-" || event.key === "_") {
        event.preventDefault();
        zoomAroundCenter(1 / ZOOM_STEP);
      } else if (event.key === "0") {
        event.preventDefault();
        resetView();
      } else if (event.key === "f" || event.key === "F") {
        event.preventDefault();
        toggleFullscreen();
      } else if (event.key === "ArrowUp") {
        event.preventDefault();
        state.y += KEY_PAN_STEP;
        applyTransform();
      } else if (event.key === "ArrowDown") {
        event.preventDefault();
        state.y -= KEY_PAN_STEP;
        applyTransform();
      } else if (event.key === "ArrowLeft") {
        event.preventDefault();
        state.x += KEY_PAN_STEP;
        applyTransform();
      } else if (event.key === "ArrowRight") {
        event.preventDefault();
        state.x -= KEY_PAN_STEP;
        applyTransform();
      }
    });

    applyTransform();
  }

  function enhanceRenderedDiagrams(root) {
    const scope = root || document;
    scope.querySelectorAll("div.mermaid").forEach(attachPanZoom);
  }

  function observeDiagrams() {
    if (activeObserver) {
      activeObserver.disconnect();
      activeObserver = null;
    }

    const contentRoot = document.querySelector(".md-content") || document.body;
    if (!contentRoot) {
      return;
    }

    enhanceRenderedDiagrams(contentRoot);

    activeObserver = new MutationObserver((mutations) => {
      for (const mutation of mutations) {
        for (const node of mutation.addedNodes) {
          if (!(node instanceof Element)) {
            continue;
          }
          if (node.matches("div.mermaid")) {
            attachPanZoom(node);
          } else if (node.querySelector) {
            node.querySelectorAll("div.mermaid").forEach(attachPanZoom);
          }
        }
      }
    });

    activeObserver.observe(contentRoot, { childList: true, subtree: true });
  }

  if (typeof window.document$ !== "undefined" && window.document$.subscribe) {
    window.document$.subscribe(() => {
      observeDiagrams();
    });
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", observeDiagrams);
  } else {
    observeDiagrams();
  }
})();
