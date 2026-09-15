/* Jesus Oneness Love Mission — interactions.
   No dependencies. Everything degrades to a readable page without JS. */
(function () {
  "use strict";

  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var $  = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  /* ---------------------------------------------------------------- Theme */
  var THEME_KEY = "jolm-theme";
  try {
    var saved = localStorage.getItem(THEME_KEY);
    if (saved === "light" || saved === "dark") {
      document.documentElement.setAttribute("data-theme", saved);
    }
  } catch (e) { /* private mode — fall back to the OS preference */ }

  function currentTheme() {
    var stamped = document.documentElement.getAttribute("data-theme");
    if (stamped) return stamped;
    return window.matchMedia("(prefers-color-scheme: light)").matches ? "light" : "dark";
  }

  var toggle = $(".theme-toggle");
  if (toggle) {
    toggle.addEventListener("click", function () {
      var next = currentTheme() === "dark" ? "light" : "dark";
      document.documentElement.setAttribute("data-theme", next);
      try { localStorage.setItem(THEME_KEY, next); } catch (e) {}
      toggle.setAttribute("aria-label", "Switch to " + (next === "dark" ? "light" : "dark") + " mode");
    });
  }

  /* --------------------------------------------------------------- Header */
  var header = $(".header");
  if (header) {
    var onScroll = function () {
      header.classList.toggle("is-stuck", window.scrollY > 12);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* --------------------------------------------------------------- Drawer */
  var drawer = $(".drawer");
  if (drawer) {
    var openDrawer = function (open) {
      drawer.classList.toggle("is-open", open);
      document.body.style.overflow = open ? "hidden" : "";
      drawer.setAttribute("aria-hidden", open ? "false" : "true");
    };
    var burger = $(".burger");
    if (burger) burger.addEventListener("click", function () { openDrawer(true); });
    var dclose = $(".drawer-close");
    if (dclose) dclose.addEventListener("click", function () { openDrawer(false); });
    $$(".drawer a").forEach(function (a) {
      a.addEventListener("click", function () { openDrawer(false); });
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") openDrawer(false);
    });
  }

  /* --------------------------------------------------------------- Toast */
  var toast = $(".toast");
  var toastTimer;
  function say(msg) {
    if (!toast) return;
    toast.textContent = msg;
    toast.classList.add("is-up");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { toast.classList.remove("is-up"); }, 2600);
  }

  /* -------------------------------------------------------------- Reveals
     Elements already on screen at load are shown immediately (no flash of
     empty page); only what is below the fold gets armed and animated. */
  var reveals = $$(".reveal");
  if (reveals.length && !reduced && "IntersectionObserver" in window) {
    var vh = window.innerHeight;
    var below = reveals.filter(function (el) {
      return el.getBoundingClientRect().top > vh * 0.92;
    });
    below.forEach(function (el) { el.classList.add("is-armed"); });

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var el = entry.target;
        var delay = parseFloat(el.getAttribute("data-delay") || "0");
        setTimeout(function () {
          el.classList.remove("is-armed");
          el.classList.add("is-in");
        }, delay);
        io.unobserve(el);
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });

    below.forEach(function (el) { io.observe(el); });
  }

  /* ------------------------------------------------------------- Count-up */
  var counters = $$("[data-count]");
  if (counters.length) {
    var runCount = function (el) {
      var target = parseInt(el.getAttribute("data-count"), 10) || 0;
      var suffix = el.getAttribute("data-suffix") || "";
      if (reduced) { el.textContent = target.toLocaleString() + suffix; return; }
      var start = performance.now();
      var dur = 1500;
      var tick = function (now) {
        var t = Math.min((now - start) / dur, 1);
        var eased = 1 - Math.pow(1 - t, 3);
        el.textContent = Math.round(target * eased).toLocaleString() + suffix;
        if (t < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
    };

    if ("IntersectionObserver" in window) {
      var cio = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          runCount(entry.target);
          cio.unobserve(entry.target);
        });
      }, { threshold: 0.4 });
      counters.forEach(function (el) { cio.observe(el); });
    } else {
      counters.forEach(runCount);
    }
  }

  /* ------------------------------------------------------- Work: filters */
  var filters = $$(".filter");
  var cards = $$(".work-card");
  filters.forEach(function (btn) {
    btn.addEventListener("click", function () {
      var cat = btn.getAttribute("data-filter");
      filters.forEach(function (b) {
        b.setAttribute("aria-pressed", String(b === btn));
      });
      cards.forEach(function (card) {
        var match = cat === "All" || card.getAttribute("data-cat") === cat;
        card.classList.toggle("is-hidden", !match);
      });
    });
  });

  /* ------------------------------------------------------ Work: lightbox */
  var lightbox = $(".lightbox");
  if (lightbox) {
    var lbTitle = $(".lightbox h3", lightbox);
    var lbCat   = $(".lightbox .lb-cat", lightbox);
    var lbMeta  = $(".lightbox .lb-meta", lightbox);
    var lbBlurb = $(".lightbox .lb-blurb", lightbox);
    var lbImg   = $(".lightbox .lb-img", lightbox);
    var lastFocus = null;

    var closeLb = function () {
      lightbox.classList.remove("is-open");
      lightbox.setAttribute("aria-hidden", "true");
      document.body.style.overflow = "";
      if (lastFocus) lastFocus.focus();
    };

    cards.forEach(function (card) {
      card.addEventListener("click", function () {
        lastFocus = card;
        lbTitle.textContent = card.getAttribute("data-title") || "";
        lbCat.textContent   = card.getAttribute("data-cat") || "";
        lbMeta.textContent  = [card.getAttribute("data-place"), card.getAttribute("data-date")]
          .filter(Boolean).join(" · ");
        lbBlurb.textContent = card.getAttribute("data-blurb") || "";

        var src = card.getAttribute("data-img");
        if (lbImg) {
          if (src) {
            lbImg.src = src;
            lbImg.alt = card.getAttribute("data-title") || "";
            lbImg.hidden = false;
          } else {
            lbImg.hidden = true;
            lbImg.removeAttribute("src");
          }
        }

        lightbox.className = "lightbox is-open " + (card.getAttribute("data-pane-class") || "pane-gold");
        lightbox.setAttribute("aria-hidden", "false");
        document.body.style.overflow = "hidden";
        var close = $(".lightbox-close", lightbox);
        if (close) close.focus();
      });
    });

    $$(".lightbox-close", lightbox).forEach(function (b) {
      b.addEventListener("click", closeLb);
    });
    lightbox.addEventListener("click", function (e) {
      if (e.target === lightbox) closeLb();
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && lightbox.classList.contains("is-open")) closeLb();
    });
  }

  /* ------------------------------------------------- Watch: click-to-play
     The poster is a facade. YouTube is not contacted at all until the visitor
     presses play, which keeps the page fast and sets no third-party cookies
     on people who never watch. */
  $$(".video-play").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var id = btn.getAttribute("data-video");
      if (!id) return;

      var frame = document.createElement("iframe");
      frame.className = "video-frame";
      frame.src = "https://www.youtube-nocookie.com/embed/" + encodeURIComponent(id) +
                  "?autoplay=1&rel=0&modestbranding=1";
      frame.title = btn.getAttribute("data-title") || "Video";
      frame.allow = "accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture";
      frame.allowFullscreen = true;
      frame.setAttribute("loading", "lazy");

      btn.replaceWith(frame);
    });
  });

  /* ----------------------------------------------------------- Give: amount */
  var amountBtns = $$(".amount");
  var customInput = $("#custom-amount");
  var impactValue = $(".impact-readout .v");
  var peso = function (n) { return "₱" + Number(n).toLocaleString(); };

  function setImpact(text) {
    if (impactValue) impactValue.textContent = text;
  }

  amountBtns.forEach(function (btn) {
    btn.addEventListener("click", function () {
      amountBtns.forEach(function (b) { b.setAttribute("aria-pressed", String(b === btn)); });
      if (customInput) customInput.value = "";
      setImpact(btn.getAttribute("data-impact") || "");
    });
  });

  if (customInput) {
    customInput.addEventListener("input", function () {
      var v = parseInt(customInput.value.replace(/[^0-9]/g, ""), 10);
      amountBtns.forEach(function (b) { b.setAttribute("aria-pressed", "false"); });
      if (!v || v <= 0) {
        setImpact("Enter an amount and we will show you what it covers.");
        return;
      }
      /* Tiers mirror GIVE_AMOUNTS in content.py. */
      var line;
      if (v < 500)       line = "Every peso counts — pooled with other gifts to buy rice and canned goods.";
      else if (v < 1000) line = "Feeds a family of five for two days.";
      else if (v < 2500) line = "Covers one week of medicine for a patient in our care.";
      else if (v < 5000) line = "Sends one child through the full Vacation Bible School.";
      else if (v < 15000) line = "Sponsors " + Math.floor(v / 5000) + " wheelchair" +
        (Math.floor(v / 5000) > 1 ? "s" : "") + ", handed over in person.";
      else               line = "Underwrites a full community outreach — food, medicine and shelter materials.";
      setImpact(peso(v) + " — " + line);
    });
  }

  /* ------------------------------------------------------ Give: reference */
  var codeEl = $(".refcode .code");
  function localCode() {
    var d = new Date();
    var stamp = String(d.getFullYear()).slice(2) + String(d.getMonth() + 1).padStart(2, "0");
    var chars = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789";
    var tail = "";
    for (var i = 0; i < 4; i++) tail += chars[Math.floor(Math.random() * chars.length)];
    return "JOLM-" + stamp + "-" + tail;
  }

  function issueCode() {
    if (!codeEl) return;
    /* Ask the Flask endpoint; fall back to a local code when the page is
       served statically (e.g. the client preview build). */
    fetch("/api/reference-code")
      .then(function (r) { return r.ok ? r.json() : Promise.reject(); })
      .then(function (d) { codeEl.textContent = d.code; })
      .catch(function () { codeEl.textContent = localCode(); });
  }
  issueCode();

  var newCodeBtn = $(".refcode .copy");
  if (newCodeBtn) {
    newCodeBtn.addEventListener("click", function () {
      copy(codeEl.textContent, "Reference code copied");
    });
  }

  /* --------------------------------------------------------- Copy to board */
  function copy(text, msg) {
    var done = function () { say(msg || "Copied"); };
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(text).then(done, function () { fallback(text, done); });
    } else {
      fallback(text, done);
    }
  }

  function fallback(text, done) {
    var ta = document.createElement("textarea");
    ta.value = text;
    ta.setAttribute("readonly", "");
    ta.style.position = "fixed";
    ta.style.opacity = "0";
    document.body.appendChild(ta);
    ta.select();
    try { document.execCommand("copy"); done(); } catch (e) { say("Press Ctrl+C to copy"); }
    document.body.removeChild(ta);
  }

  $$(".acct-row .copy").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var val = btn.getAttribute("data-copy") || "";
      copy(val, (btn.getAttribute("data-label") || "Details") + " copied");
      btn.classList.add("is-done");
      var label = $(".copy-label", btn);
      if (label) {
        var was = label.textContent;
        label.textContent = "Copied";
        setTimeout(function () { label.textContent = was; btn.classList.remove("is-done"); }, 1800);
      }
    });
  });

  /* ------------------------------------------- Hero: dust motes in the light
     Cathedral light catches dust. Cheap canvas, pauses when off-screen. */
  var canvas = document.getElementById("motes");
  if (canvas && !reduced) {
    var ctx = canvas.getContext("2d");
    var motes = [];
    var raf = null;
    var w = 0, h = 0;

    function size() {
      var dpr = Math.min(window.devicePixelRatio || 1, 2);
      var rect = canvas.parentElement.getBoundingClientRect();
      w = rect.width; h = rect.height;
      canvas.width = w * dpr;
      canvas.height = h * dpr;
      canvas.style.width = w + "px";
      canvas.style.height = h + "px";
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    }

    function seed() {
      var count = Math.round(Math.min(w, 1400) / 16);
      motes = [];
      for (var i = 0; i < count; i++) {
        motes.push({
          x: Math.random() * w,
          y: Math.random() * h,
          r: Math.random() * 1.6 + 0.35,
          vy: -(Math.random() * 0.18 + 0.04),
          vx: (Math.random() - 0.5) * 0.12,
          a: Math.random() * 0.5 + 0.12,
          p: Math.random() * Math.PI * 2
        });
      }
    }

    function gold() {
      return getComputedStyle(document.documentElement).getPropertyValue("--gold").trim() || "#E3B44A";
    }

    var fill = gold();

    function frame(t) {
      ctx.clearRect(0, 0, w, h);
      for (var i = 0; i < motes.length; i++) {
        var m = motes[i];
        m.y += m.vy;
        m.x += m.vx + Math.sin(t / 2600 + m.p) * 0.14;
        if (m.y < -6) { m.y = h + 6; m.x = Math.random() * w; }
        if (m.x < -6) m.x = w + 6;
        if (m.x > w + 6) m.x = -6;
        var twinkle = 0.65 + Math.sin(t / 1100 + m.p) * 0.35;
        ctx.globalAlpha = m.a * twinkle;
        ctx.fillStyle = fill;
        ctx.beginPath();
        ctx.arc(m.x, m.y, m.r, 0, Math.PI * 2);
        ctx.fill();
      }
      ctx.globalAlpha = 1;
      raf = requestAnimationFrame(frame);
    }

    size(); seed();
    raf = requestAnimationFrame(frame);

    var rt;
    window.addEventListener("resize", function () {
      clearTimeout(rt);
      rt = setTimeout(function () { size(); seed(); }, 180);
    });

    /* Stop drawing once the hero scrolls away. */
    if ("IntersectionObserver" in window) {
      new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting && raf === null) {
            fill = gold();
            raf = requestAnimationFrame(frame);
          } else if (!e.isIntersecting && raf !== null) {
            cancelAnimationFrame(raf);
            raf = null;
          }
        });
      }, { threshold: 0 }).observe(canvas);
    }

    /* Re-read the accent when the theme flips. */
    if (toggle) toggle.addEventListener("click", function () {
      setTimeout(function () { fill = gold(); }, 30);
    });
  }
})();
