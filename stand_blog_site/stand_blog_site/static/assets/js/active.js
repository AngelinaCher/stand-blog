const currentPath = window.location.pathname;
const navItems = document.querySelectorAll(".nav-item");

navItems.forEach(function (item) {
  const link = item.querySelector(".nav-link");
  let linkPath = link.getAttribute("href");

  linkPath = linkPath.replace(/^\//, "");

  if (currentPath === "/" + linkPath) {
    item.classList.add("active");
  } else {
    item.classList.remove("active");
  }
});
