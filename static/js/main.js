// ── Hamburger Menu Toggle ──────────────────────────────────────────────────────
// Toggles mobile navigation menu open/close
(() => {
  const hamburgerBtn = document.getElementById("hamburgerBtn");
  const navMenu = document.getElementById("navMenu");
  const headerRight = document.querySelector(".header-right");
  
  if (!hamburgerBtn || !navMenu) return;
  
  hamburgerBtn.addEventListener("click", () => {
    const isOpen = navMenu.classList.toggle("nav-open");
    hamburgerBtn.setAttribute("aria-expanded", isOpen);
  });
  
  // Close menu when a nav link is clicked
  navMenu.querySelectorAll("a").forEach(link => {
    link.addEventListener("click", () => {
      navMenu.classList.remove("nav-open");
      hamburgerBtn.setAttribute("aria-expanded", false);
    });
  });
  
  // Move header-right into nav on mobile
  const moveHeaderRight = () => {
    if (window.innerWidth < 768) {
      if (headerRight.parentElement === document.querySelector(".header-container")) {
        navMenu.appendChild(headerRight);
      }
    } else {
      if (headerRight.parentElement === navMenu) {
        document.querySelector(".header-container").appendChild(headerRight);
      }
    }
  };
  
  moveHeaderRight();
  window.addEventListener("resize", moveHeaderRight);
})();

// ── API Status Check ──────────────────────────────────────────────────────────
// Updates the API status indicator in the header with real-time connection status
(async () => {
  const el = document.getElementById("apiStatus");
  if (!el) return;
  
  try {
    const res = await fetch("/api/summary");
    const data = await res.json();
    
    if (data.error) {
      el.textContent = "⚠️ API not configured";
      el.style.color = "#F57C00";
    } else {
      el.textContent = `✅ API OK — ${data.total} securities`;
      el.style.color = "#00AA44";
    }
  } catch (e) {
    el.textContent = "❌ API unreachable";
    el.style.color = "#CC0000";
  }
})();

