const themeToggleIcon = document.querySelector('#theme-toggle-button i'),
      footer = document.querySelector('#main-footer');
themeToggleIcon.addEventListener('click', themeToggler);


function themeToggler() {
  if (themeToggleIcon.classList.contains('dark-theme-icon')) {
    themeToggleIcon.classList.remove('dark-theme-icon');
    themeToggleIcon.classList.add('light-theme-icon');
    document.documentElement.style.setProperty('--bg-color', 'white');
    document.documentElement.style.setProperty('--fg-color', 'black');
  }
  else {
    themeToggleIcon.classList.remove('light-theme-icon');
    themeToggleIcon.classList.add('dark-theme-icon');
    document.documentElement.style.setProperty('--bg-color', '#252525');
    document.documentElement.style.setProperty('--fg-color', 'white');
  }
}

window.onload = function () {
  console.log('done');
}

// show footer if user scrolls under all elements
window.addEventListener("scroll", function () {
  if (window.pageYOffset > 500) {
    footer.classList.add('footer-visible');
    footer.classList.remove('footer-invisible');
  } else {
    footer.classList.remove('footer-visible');
    footer.classList.add('footer-invisible');
  }
});