const themeToggleIcon = document.querySelector('#theme-toggle-button i');
themeToggleIcon.addEventListener('click',themeToggler);


function themeToggler() {
    if (themeToggleIcon.classList.contains('dark-theme-icon')) {
      themeToggleIcon.classList.remove('dark-theme-icon');
      themeToggleIcon.classList.add('light-theme-icon');
      document.documentElement.style.setProperty('--bg-color', 'white');
      document.documentElement.style.setProperty('--fg-color','black');
    }
    else {
      themeToggleIcon.classList.remove('light-theme-icon');
      themeToggleIcon.classList.add('dark-theme-icon');
      document.documentElement.style.setProperty('--bg-color', '#252525');
      document.documentElement.style.setProperty('--fg-color','white');
    }
  }
  
  window.onload = function() {
    console.log('done');
  }