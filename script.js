const themeToggleIcon = document.querySelector('#theme-toggle-button i');
themeToggleIcon.addEventListener('click',themeToggler);


function themeToggler() {
    if (themeToggleIcon.classList.contains('dark-theme-icon')) {
      themeToggleIcon.classList.remove('dark-theme-icon');
      themeToggleIcon.classList.add('light-theme-icon');
    }
    else {
      themeToggleIcon.classList.remove('light-theme-icon');
      themeToggleIcon.classList.add('dark-theme-icon');
    }
  }
  
  window.onload = function() {
    console.log('done');
  }