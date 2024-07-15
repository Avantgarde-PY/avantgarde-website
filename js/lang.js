document.addEventListener('DOMContentLoaded', function() {
    const languageOptions = document.querySelectorAll('.language-option');
  
    languageOptions.forEach(option => {
      option.addEventListener('click', function(event) {
        event.preventDefault();
        document.querySelector('.language-option.selected').classList.remove('selected');
        this.classList.add('selected');
        console.log('Selected language:', this.getAttribute('data-lang'));
      });
    });
  });
