// Main JavaScript functionality for AI Governance

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all components
    initializeComponents();
    
    // Add smooth scrolling for anchor links
    addSmoothScrolling();
    
    // Add scroll animations
    addScrollAnimations();
    
    // Add form handling
    addFormHandling();
    
    // Initialize modal
    initializeModal();
});

function initializeComponents() {
    // Initialize feather icons
    if (typeof feather !== 'undefined') {
        feather.replace();
    }
    
    // Add loading states to buttons
    addLoadingStates();
}

function addSmoothScrolling() {
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

function addScrollAnimations() {
    // Intersection Observer for fade-in animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-up');
            }
        });
    }, observerOptions);
    
    // Observe elements for animation
    document.querySelectorAll('.bg-white, .hero-content, section').forEach(el => {
        observer.observe(el);
    });
}

function addLoadingStates() {
    // Add loading states to CTA buttons
    document.querySelectorAll('a[href="#contact"], button[type="submit"]').forEach(button => {
        button.addEventListener('click', function(e) {
            // Add loading state
            this.classList.add('loading');
            
            // In a real app, you'd handle form submission here
            setTimeout(() => {
                this.classList.remove('loading');
            }, 1000);
        });
    });
}

function addFormHandling() {
    // Handle contact form submissions (when implemented)
    const contactForms = document.querySelectorAll('form');
    contactForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Add form validation
            const formData = new FormData(this);
            const data = Object.fromEntries(formData);
            
            // Basic validation
            if (!data.email || !data.name) {
                showNotification('Please fill in all required fields', 'error');
                return;
            }
            
            // Show success message
            showNotification('Thank you! We\'ll be in touch soon.', 'success');
            this.reset();
        });
    });
}

// Modal functionality
function initializeModal() {
    const modal = document.getElementById('contactModal');
    if (!modal) return;
    
    const closeModal = document.getElementById('closeModal');
    const contactForm = document.getElementById('contactForm');
    
    // Open modal when clicking Contact buttons
    document.querySelectorAll('a[href="#contact"]').forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            if (modal) {
                modal.classList.remove('hidden');
                document.body.style.overflow = 'hidden'; // Prevent background scrolling
            }
        });
    });
    
    // Close modal
    if (closeModal) {
        closeModal.addEventListener('click', function() {
            modal.classList.add('hidden');
            document.body.style.overflow = 'auto';
        });
    }
    
    // Close modal when clicking outside
    modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            modal.classList.add('hidden');
            document.body.style.overflow = 'auto';
        }
    });
    
    // Handle form submission
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const formData = new FormData(this);
            const data = Object.fromEntries(formData);
            
            // Basic validation
            if (!data.email || !data.name) {
                showNotification('Please fill in all required fields', 'error');
                return;
            }
            
            // Show success message
            showNotification('Thank you! We\'ll contact you soon.', 'success');
            
            // Close modal and reset form
            modal.classList.add('hidden');
            document.body.style.overflow = 'auto';
            this.reset();
            
            // In a real implementation, you'd send this data to your backend
            console.log('Contact form submitted:', data);
        });
    }
}

function showNotification(message, type = 'info') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `fixed top-20 right-4 z-50 p-4 rounded-lg shadow-lg transition-all duration-300 transform translate-x-full ${
        type === 'success' ? 'bg-green-500 text-white' : 
        type === 'error' ? 'bg-red-500 text-white' : 
        'bg-blue-500 text-white'
    }`;
    notification.textContent = message;
    
    document.body.appendChild(notification);
    
    // Animate in
    setTimeout(() => {
        notification.classList.remove('translate-x-full');
    }, 100);
    
    // Remove after 3 seconds
    setTimeout(() => {
        notification.classList.add('translate-x-full');
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 3000);
}

// Utility functions
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Add scroll-based navbar styling
window.addEventListener('scroll', debounce(() => {
    const navbar = document.querySelector('nav');
    if (navbar) {
        if (window.scrollY > 100) {
            navbar.classList.add('bg-opacity-95', 'backdrop-blur-sm');
        } else {
            navbar.classList.remove('bg-opacity-95', 'backdrop-blur-sm');
        }
    }
}, 10));

// Add card hover effects
document.querySelectorAll('.bg-white.p-8.rounded-xl.shadow-lg').forEach(card => {
    card.addEventListener('mouseenter', function() {
        this.classList.add('card-hover');
    });
    
    card.addEventListener('mouseleave', function() {
        this.classList.remove('card-hover');
    });
});

