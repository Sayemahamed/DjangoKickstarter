// Theme management
document.addEventListener('DOMContentLoaded', function() {
    // Theme selector functionality
    const themeSelector = document.getElementById('theme-selector');
    const html = document.documentElement;
    
    // Load saved theme from localStorage
    const savedTheme = localStorage.getItem('selectedTheme') || 'theme-green';
    html.className = savedTheme;
    if (themeSelector) {
        themeSelector.value = savedTheme === '' ? 'default' : savedTheme;
    }

    // Handle theme changes
    if (themeSelector) {
        themeSelector.addEventListener('change', function() {
            const selectedTheme = this.value;
            html.className = selectedTheme === 'default' ? '' : selectedTheme;
            localStorage.setItem('selectedTheme', html.className);
        });
    }

    // Mobile menu functionality
    const menuButton = document.querySelector('.mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');

    if (menuButton && mobileMenu) {
        menuButton.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
        });
    }
});