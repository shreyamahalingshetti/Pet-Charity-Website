// =====================================================
// PawsOfHope — Mode Switching & Interactive JS
// =====================================================

document.addEventListener('DOMContentLoaded', function () {

    // ---------- Mode Toggle ----------
    const modeSwitch = document.getElementById('mode-switch');
    const body = document.getElementById('app-body');

    if (modeSwitch) {
        modeSwitch.addEventListener('change', function () {
            const newMode = this.checked ? 'dog' : 'cat';

            // Update body class immediately for instant visual feedback
            body.classList.remove('cat-mode', 'dog-mode');
            body.classList.add(newMode + '-mode');

            // Get CSRF token
            const csrfToken = getCSRFToken();

            // Send mode to server
            fetch('/set-mode/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-CSRFToken': csrfToken
                },
                body: 'mode=' + newMode
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'ok') {
                    // Reload page to update content
                    window.location.reload();
                }
            })
            .catch(err => {
                console.error('Mode switch error:', err);
                // Reload anyway to sync
                window.location.reload();
            });
        });
    }

    // ---------- CSRF Token Helper ----------
    function getCSRFToken() {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith('csrftoken=')) {
                return cookie.substring('csrftoken='.length);
            }
        }
        // Fallback: look for hidden input
        const input = document.querySelector('[name=csrfmiddlewaretoken]');
        return input ? input.value : '';
    }

    // ---------- Hamburger Menu ----------
    const hamburger = document.getElementById('hamburger');
    const navLinks = document.getElementById('nav-links');

    if (hamburger && navLinks) {
        hamburger.addEventListener('click', function () {
            navLinks.classList.toggle('active');
            // Animate hamburger
            this.classList.toggle('active');
        });

        // Close menu on link click
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                navLinks.classList.remove('active');
                hamburger.classList.remove('active');
            });
        });
    }

    // ---------- Navbar Scroll Effect ----------
    const navbar = document.getElementById('main-nav');
    let lastScroll = 0;

    window.addEventListener('scroll', function () {
        const currentScroll = window.scrollY;

        if (currentScroll > 50) {
            navbar.style.boxShadow = '0 4px 20px rgba(0,0,0,0.1)';
        } else {
            navbar.style.boxShadow = 'none';
        }

        lastScroll = currentScroll;
    });

    // ---------- Scroll Animations ----------
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function (entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Animate elements on scroll
    const animateElements = document.querySelectorAll(
        '.feature-card, .pet-card, .awareness-card, .stat-card, ' +
        '.about-card, .service-item, .gallery-item, .breakdown-item, .contact-item, .fact-item'
    );

    animateElements.forEach((el, index) => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = `opacity 0.6s ease ${index * 0.08}s, transform 0.6s ease ${index * 0.08}s, 
                               border-color 0.3s ease, box-shadow 0.4s ease`;
        observer.observe(el);
    });

    // ---------- Auto-dismiss Alerts ----------
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.opacity = '0';
            alert.style.transform = 'translateX(100%)';
            setTimeout(() => alert.remove(), 400);
        }, 5000);
    });

    // ---------- Quick Amount Button Active State ----------
    const quickBtns = document.querySelectorAll('.quick-amt-btn');
    quickBtns.forEach(btn => {
        btn.addEventListener('click', function () {
            quickBtns.forEach(b => b.style.borderColor = '');
            this.style.borderColor = 'var(--accent)';
        });
    });
});
