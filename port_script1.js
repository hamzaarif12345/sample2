const navbar = document.querySelector('.navbar');
const scrollBtn = document.querySelector('.scroll-up-btn');
const menuToggle = document.querySelector('.menu-toggle');
const menu = document.querySelector('.menu');
const menuLinks = document.querySelectorAll('.menu a');
const typingTarget = document.querySelector('.typing');

function handleScrollUI() {
    if (window.scrollY > 16) {
        navbar.classList.add('sticky');
    } else {
        navbar.classList.remove('sticky');
    }

    if (window.scrollY > 420) {
        scrollBtn.classList.add('show');
    } else {
        scrollBtn.classList.remove('show');
    }
}

window.addEventListener('scroll', handleScrollUI);
handleScrollUI();

scrollBtn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
});

if (menuToggle) {
    menuToggle.addEventListener('click', () => {
        const isOpen = menu.classList.toggle('open');
        menuToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });
}

menuLinks.forEach((link) => {
    link.addEventListener('click', () => {
        menu.classList.remove('open');
        menuToggle.setAttribute('aria-expanded', 'false');
    });
});

const sections = [...document.querySelectorAll('section[id]')];
const sectionObserver = new IntersectionObserver(
    (entries) => {
        entries.forEach((entry) => {
            if (!entry.isIntersecting) {
                return;
            }

            const id = entry.target.getAttribute('id');
            menuLinks.forEach((link) => {
                const isMatch = link.getAttribute('href') === `#${id}`;
                link.classList.toggle('active', isMatch);
            });
        });
    },
    { threshold: 0.45 }
);

sections.forEach((section) => sectionObserver.observe(section));

const revealNodes = document.querySelectorAll('.reveal');
const revealObserver = new IntersectionObserver(
    (entries, observer) => {
        entries.forEach((entry) => {
            if (!entry.isIntersecting) {
                return;
            }

            entry.target.classList.add('visible');
            observer.unobserve(entry.target);
        });
    },
    { threshold: 0.12 }
);

revealNodes.forEach((node) => revealObserver.observe(node));

const roles = ['Programmer', 'Software Developer', 'Web Developer', 'AI/ML Enthusiast', 'Data Analyst'];
let roleIndex = 0;
let letterIndex = 0;
let isDeleting = false;

function typeRole() {
    if (!typingTarget) {
        return;
    }

    const currentRole = roles[roleIndex];

    if (isDeleting) {
        letterIndex -= 1;
    } else {
        letterIndex += 1;
    }

    typingTarget.textContent = currentRole.slice(0, letterIndex);

    let delay = isDeleting ? 55 : 95;

    if (!isDeleting && letterIndex === currentRole.length) {
        delay = 1400;
        isDeleting = true;
    } else if (isDeleting && letterIndex === 0) {
        isDeleting = false;
        roleIndex = (roleIndex + 1) % roles.length;
        delay = 360;
    }

    setTimeout(typeRole, delay);
}

typeRole();
