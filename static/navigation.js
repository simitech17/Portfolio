(() => {
    const navigation = document.querySelector('.site-nav');
    if (!navigation) return;

    const toggle = navigation.querySelector('.nav-toggle');
    const links = navigation.querySelector('.nav-links');
    const label = toggle.querySelector('.nav-toggle-label');
    const mobile = window.matchMedia('(max-width: 980px)');

    function setOpen(open, restoreFocus = false) {
        toggle.setAttribute('aria-expanded', String(open));
        label.textContent = open ? 'Close' : 'Menu';
        navigation.classList.toggle('menu-open', open);
        if (restoreFocus) toggle.focus();
    }

    toggle.hidden = false;
    navigation.classList.add('navigation-ready');

    toggle.addEventListener('click', () => {
        setOpen(toggle.getAttribute('aria-expanded') !== 'true');
    });

    links.addEventListener('click', event => {
        const link = event.target.closest('a');
        if (!link) return;
        // Return focus before the disclosure is hidden, then focus in-page targets.
        if (mobile.matches) setOpen(false, true);
        const destination = new URL(link.href, window.location.href);
        if (destination.pathname === window.location.pathname && destination.hash) {
            const target = document.getElementById(destination.hash.slice(1));
            if (target) {
                target.setAttribute('tabindex', '-1');
                target.focus({ preventScroll: true });
            }
        }
    });

    document.addEventListener('keydown', event => {
        if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
            setOpen(false, true);
        }
    });

    document.addEventListener('click', event => {
        if (!navigation.contains(event.target)) setOpen(false);
    });

    mobile.addEventListener('change', () => {
        const focusWillHide = mobile.matches && links.contains(document.activeElement);
        const toggleHadFocus = document.activeElement === toggle;
        setOpen(false, focusWillHide);
        if (!mobile.matches && toggleHadFocus) links.querySelector('a').focus();
    });
})();
