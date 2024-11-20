// Theme Management
function initializeTheme() {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        document.documentElement.className = savedTheme;
        document.getElementById('theme-selector').value = savedTheme;
        const mobileSelector = document.getElementById('mobile-theme-selector');
        if (mobileSelector) {
            mobileSelector.value = savedTheme;
        }
    }
}

function handleThemeChange(event) {
    const theme = event.target.value;
    document.documentElement.className = theme;
    localStorage.setItem('theme', theme);
    
    // Sync the other theme selector
    const isDesktop = event.target.id === 'theme-selector';
    const otherSelector = document.getElementById(isDesktop ? 'mobile-theme-selector' : 'theme-selector');
    if (otherSelector) {
        otherSelector.value = theme;
    }
}

document.addEventListener('DOMContentLoaded', () => {
    // Initialize theme
    initializeTheme();
    
    // Setup theme selectors
    const themeSelector = document.getElementById('theme-selector');
    const mobileThemeSelector = document.getElementById('mobile-theme-selector');
    
    if (themeSelector) {
        themeSelector.addEventListener('change', handleThemeChange);
    }
    if (mobileThemeSelector) {
        mobileThemeSelector.addEventListener('change', handleThemeChange);
    }
    
    // Mobile menu toggle
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');
    
    if (mobileMenuButton && mobileMenu) {
        mobileMenuButton.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
        });
    }
});