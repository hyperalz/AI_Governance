// Navbar Component
class CustomNavbar extends HTMLElement {
    connectedCallback() {
        this.innerHTML = `
            <nav class="bg-white shadow-lg fixed w-full top-0 z-50">
                <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div class="flex justify-between h-16">
                        <div class="flex items-center">
                            <div class="flex-shrink-0">
                                <h1 class="text-2xl font-bold text-blue-600">AI Governance</h1>
                            </div>
                        </div>
                        <div class="hidden md:flex items-center space-x-8">
                            <a href="#overview" class="text-gray-700 hover:text-blue-600 px-3 py-2 rounded-md text-sm font-medium transition duration-300">Overview</a>
                            <a href="#framework" class="text-gray-700 hover:text-blue-600 px-3 py-2 rounded-md text-sm font-medium transition duration-300">Framework</a>
                            <a href="#principles" class="text-gray-700 hover:text-blue-600 px-3 py-2 rounded-md text-sm font-medium transition duration-300">Principles</a>
                            <a href="#products" class="text-gray-700 hover:text-blue-600 px-3 py-2 rounded-md text-sm font-medium transition duration-300">Products</a>
                            <a href="#contact" class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md text-sm font-medium transition duration-300">Contact</a>
                        </div>
                        <div class="md:hidden flex items-center">
                            <button id="mobile-menu-button" class="text-gray-700 hover:text-blue-600 focus:outline-none focus:text-blue-600">
                                <i data-feather="menu" class="w-6 h-6"></i>
                            </button>
                        </div>
                    </div>
                </div>
                <div id="mobile-menu" class="md:hidden hidden">
                    <div class="px-2 pt-2 pb-3 space-y-1 sm:px-3 bg-white border-t">
                        <a href="#overview" class="text-gray-700 hover:text-blue-600 block px-3 py-2 rounded-md text-base font-medium">Overview</a>
                        <a href="#framework" class="text-gray-700 hover:text-blue-600 block px-3 py-2 rounded-md text-base font-medium">Framework</a>
                        <a href="#principles" class="text-gray-700 hover:text-blue-600 block px-3 py-2 rounded-md text-base font-medium">Principles</a>
                        <a href="#products" class="text-gray-700 hover:text-blue-600 block px-3 py-2 rounded-md text-base font-medium">Products</a>
                        <a href="#contact" class="bg-blue-600 hover:bg-blue-700 text-white block px-3 py-2 rounded-md text-base font-medium">Contact</a>
                    </div>
                </div>
            </nav>
        `;
        
        // Add mobile menu functionality
        const mobileMenuButton = this.querySelector('#mobile-menu-button');
        const mobileMenu = this.querySelector('#mobile-menu');
        
        if (mobileMenuButton && mobileMenu) {
            mobileMenuButton.addEventListener('click', () => {
                mobileMenu.classList.toggle('hidden');
            });
        }
    }
}

customElements.define('custom-navbar', CustomNavbar);

