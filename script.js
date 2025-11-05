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

// Demo output simulation
function runDemo() {
    const outputDiv = document.getElementById('demo-output');
    if (!outputDiv) return;
    
    // Clear previous output
    outputDiv.innerHTML = '';
    
    // Demo output text - improved readability
    const demoOutput = `
═══════════════════════════════════════════════════════════════════
   GitHub Copilot Auditor
═══════════════════════════════════════════════════════════════════


🔍 Fetching repositories for organization: TechCorp-Dev
   Found 14 repositories (page 1)...
   
✅ Total repositories found: 14


🔎 Auditing 14 repositories for Copilot usage...

   [ 1/14] 🔴 TechCorp-Dev/public-api
           Risk: CRITICAL
           
   [ 2/14] 🔴 TechCorp-Dev/marketing-site
           Risk: CRITICAL
           
   [ 3/14] 🟡 TechCorp-Dev/payment-processing
           Risk: HIGH
           
   [ 4/14] 🟡 TechCorp-Dev/user-database
           Risk: HIGH
           
   [ 5/14] 🟡 TechCorp-Dev/internal-admin-tools
           Risk: HIGH
           
   [ 6/14] 🟡 TechCorp-Dev/legacy-monolith
           Risk: HIGH
           
   [ 7/14] 🟢 TechCorp-Dev/documentation
           Risk: LOW
           
   [ 8/14] 🟢 TechCorp-Dev/test-suite
           Risk: LOW
           
   [ 9/14] 🟢 TechCorp-Dev/frontend-app
           Risk: LOW
           
   [10/14] 🟢 TechCorp-Dev/infrastructure
           Risk: LOW
           
   [11/14] 🟢 TechCorp-Dev/design-system
           Risk: LOW
           
   [12/14] 🟢 TechCorp-Dev/analytics-dashboard
           Risk: LOW
           
   [13/14] 🟢 TechCorp-Dev/mobile-app
           Risk: LOW
           
   [14/14] 🟢 TechCorp-Dev/ci-cd-pipelines
           Risk: LOW


✅ Report generated: github_copilot_audit_techcorp-dev_20241104.csv
   Total repositories audited: 14


📊 Risk Summary:
───────────────────────────────────────────────────────────────────
   CRITICAL:  2 repositories  (14.3%)
   HIGH:      4 repositories  (28.6%)
   LOW:       8 repositories  (57.1%)


⚠️  IMPORTANT FINDINGS:
───────────────────────────────────────────────────────────────────


🔴 CRITICAL RISK: 2 repositories

   Copilot is enabled on PUBLIC repositories.
   This poses significant IP and compliance risks.

   Affected repositories:
   
   • TechCorp-Dev/public-api
     └─ Main public API - sensitive endpoints exposed
     └─ URL: https://github.com/TechCorp-Dev/public-api

   • TechCorp-Dev/marketing-site
     └─ Public marketing website with embedded secrets
     └─ URL: https://github.com/TechCorp-Dev/marketing-site

   💡 RECOMMENDED ACTIONS:
   1. Immediately review what code is being processed by Copilot
   2. Consider disabling Copilot on public repositories
   3. Move sensitive code to private repositories
   4. Review and remove any secrets or sensitive data
   5. Implement code scanning for exposed credentials


🟡 HIGH RISK: 4 repositories

   Copilot is enabled on PRIVATE repositories.
   Potential IP/code leakage risk with sensitive codebases.

   Affected repositories:
   
   • TechCorp-Dev/payment-processing
     └─ Payment gateway integration - sensitive financial code

   • TechCorp-Dev/user-database
     └─ User management system with PII handling

   • TechCorp-Dev/internal-admin-tools
     └─ Internal admin dashboard

   • TechCorp-Dev/legacy-monolith
     └─ Legacy system with outdated dependencies

   💡 RECOMMENDED ACTIONS:
   1. Review Copilot usage policies for private repos
   2. Ensure team members understand data handling
   3. Consider enabling Copilot ignore files (.copilotignore)
   4. Monitor for any unusual Copilot activity
   5. Document approved use cases


🟢 LOW RISK: 8 repositories

   Copilot is disabled or not applicable.
   No immediate action required.


═══════════════════════════════════════════════════════════════════
✅ Audit complete!
═══════════════════════════════════════════════════════════════════


📄 Full report saved to: github_copilot_audit_techcorp-dev_20241104.csv


📋 Next Steps:
   1. Review the CSV report for detailed findings
   2. Prioritize CRITICAL and HIGH risk repositories
   3. Implement remediation actions
   4. Establish ongoing monitoring and governance
   5. Update AI governance policies based on findings


`;

    // Type out the demo with animation
    let i = 0;
    const speed = 2; // milliseconds per character
    
    function typeWriter() {
        if (i < demoOutput.length) {
            // Use textContent to preserve whitespace and formatting
            outputDiv.textContent = demoOutput.substring(0, i + 1);
            i++;
            setTimeout(typeWriter, speed);
            // Auto-scroll to bottom
            outputDiv.scrollTop = outputDiv.scrollHeight;
        } else {
            // Add cursor blink effect
            outputDiv.textContent = demoOutput + '█';
        }
    }
    
    typeWriter();
}

// Make runDemo available globally
window.runDemo = runDemo;

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

