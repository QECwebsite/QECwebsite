document.addEventListener('DOMContentLoaded', () => {
  const navs = document.querySelectorAll('.site-nav');
  const closeMenu = (nav, toggle, menu) => {
    nav.classList.remove('is-open');
    toggle.setAttribute('aria-expanded', 'false');
    menu.dataset.open = 'false';
    document.body.classList.remove('nav-open');
  };

  navs.forEach((nav) => {
    const toggle = nav.querySelector('.nav-toggle');
    const menu = nav.querySelector('#nav-menu');

    if (!toggle || !menu) {
      return;
    }

    // Ensure default state is closed
    closeMenu(nav, toggle, menu);

    toggle.addEventListener('click', () => {
      const isOpen = nav.classList.toggle('is-open');
      const state = isOpen ? 'true' : 'false';
      toggle.setAttribute('aria-expanded', state);
      menu.dataset.open = state;
      document.body.classList.toggle('nav-open', isOpen);
    });

    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' && nav.classList.contains('is-open')) {
        closeMenu(nav, toggle, menu);
        toggle.focus();
      }
    });

    menu.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => {
        if (nav.classList.contains('is-open')) {
          closeMenu(nav, toggle, menu);
        }
      });
    });

    const mq = window.matchMedia('(min-width: 1001px)');
    const handleChange = (event) => {
      if (event.matches) {
        closeMenu(nav, toggle, menu);
      }
    };

    if (typeof mq.addEventListener === 'function') {
      mq.addEventListener('change', handleChange);
    } else if (typeof mq.addListener === 'function') {
      mq.addListener(handleChange);
    }
  });
});
