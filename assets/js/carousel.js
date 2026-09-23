// Carousels, lightbox, and the signup form.

class Carousel {
    constructor(element) {
        this.carousel = element;
        this.slides = element.querySelectorAll('.carousel-slide');
        this.prevBtn = element.querySelector('.prev');
        this.nextBtn = element.querySelector('.next');
        this.indicatorsContainer = element.querySelector('.carousel-indicators');
        this.currentIndex = 0;
        this.init();
    }

    init() {
        this.createIndicators();
        this.showSlide(0);

        this.slides.forEach((slide, index) => {
            const img = slide.querySelector('img');
            if (img) {
                img.addEventListener('click', () => {
                    if (window.lightbox) window.lightbox.open(this, index);
                });
            }
        });

        if (this.prevBtn) this.prevBtn.addEventListener('click', () => this.prevSlide());
        if (this.nextBtn) this.nextBtn.addEventListener('click', () => this.nextSlide());

        // Arrow keys move only the carousel the pointer is over.
        this.carousel.addEventListener('mouseenter', () => { Carousel.hovered = this; });
        this.carousel.addEventListener('mouseleave', () => { if (Carousel.hovered === this) Carousel.hovered = null; });

        let touchStartX = 0;
        this.carousel.addEventListener('touchstart', (e) => {
            touchStartX = e.changedTouches[0].screenX;
        }, { passive: true });
        this.carousel.addEventListener('touchend', (e) => {
            this.handleSwipe(touchStartX, e.changedTouches[0].screenX);
        }, { passive: true });
    }

    createIndicators() {
        if (this.slides.length < 2) {
            this.indicatorsContainer.classList.add('single');
            this.indicators = [];
            return;
        }
        this.slides.forEach((_, index) => {
            const indicator = document.createElement('span');
            indicator.classList.add('indicator');
            indicator.setAttribute('role', 'button');
            indicator.setAttribute('aria-label', 'Slide ' + (index + 1));
            indicator.addEventListener('click', () => this.showSlide(index));
            this.indicatorsContainer.appendChild(indicator);
        });
        this.indicators = this.indicatorsContainer.querySelectorAll('.indicator');
    }

    showSlide(index) {
        this.slides.forEach(slide => slide.classList.remove('active'));
        this.indicators.forEach(indicator => indicator.classList.remove('active'));
        this.slides[index].classList.add('active');
        if (this.indicators[index]) this.indicators[index].classList.add('active');
        this.currentIndex = index;
    }

    nextSlide() { this.showSlide((this.currentIndex + 1) % this.slides.length); }
    prevSlide() { this.showSlide((this.currentIndex - 1 + this.slides.length) % this.slides.length); }

    handleSwipe(startX, endX) {
        const diff = startX - endX;
        if (Math.abs(diff) > 50) {
            if (diff > 0) this.nextSlide(); else this.prevSlide();
        }
    }
}
Carousel.hovered = null;

class Lightbox {
    constructor() {
        this.modal = document.getElementById('lightbox-modal');
        this.image = document.getElementById('lightbox-image');
        this.caption = document.getElementById('lightbox-caption');
        this.closeBtn = this.modal.querySelector('.lightbox-close');
        this.prevBtn = this.modal.querySelector('.lightbox-btn.prev');
        this.nextBtn = this.modal.querySelector('.lightbox-btn.next');
        this.currentCarousel = null;
        this.currentIndex = 0;
        this.init();
    }

    init() {
        this.closeBtn.addEventListener('click', () => this.close());
        this.modal.addEventListener('click', (e) => {
            if (e.target === this.modal || e.target === this.modal.querySelector('.lightbox-content')) this.close();
        });
        this.prevBtn.addEventListener('click', (e) => { e.stopPropagation(); this.prev(); });
        this.nextBtn.addEventListener('click', (e) => { e.stopPropagation(); this.next(); });
    }

    isOpen() { return this.modal.classList.contains('active'); }

    open(carousel, index) {
        this.currentCarousel = carousel;
        this.currentIndex = index;
        this.updateContent();
        this.modal.classList.add('active');
        const multi = carousel.slides.length > 1;
        this.prevBtn.style.display = multi ? '' : 'none';
        this.nextBtn.style.display = multi ? '' : 'none';
        document.body.style.overflow = 'hidden';
        this.closeBtn.focus();
    }

    close() {
        this.modal.classList.remove('active');
        document.body.style.overflow = '';
    }

    updateContent() {
        const slide = this.currentCarousel.slides[this.currentIndex];
        const img = slide.querySelector('img');
        const captionElement = slide.querySelector('.caption');
        this.image.src = img.src;
        this.image.alt = img.alt;
        this.caption.textContent = captionElement ? captionElement.textContent : '';
        this.currentCarousel.showSlide(this.currentIndex);
    }

    next() {
        this.currentIndex = (this.currentIndex + 1) % this.currentCarousel.slides.length;
        this.updateContent();
    }

    prev() {
        this.currentIndex = (this.currentIndex - 1 + this.currentCarousel.slides.length) % this.currentCarousel.slides.length;
        this.updateContent();
    }
}

function initSignup() {
    const form = document.querySelector('.signup');
    if (!form) return;
    const status = form.querySelector('.signup-status');
    const button = form.querySelector('button');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        if (form.action.includes('YOUR_FORM_ID')) {
            status.textContent = 'Signup is not wired up yet. Email elvin@arbutus.audio and you will be added by hand.';
            return;
        }
        button.disabled = true;
        status.textContent = 'Sending…';
        try {
            const res = await fetch(form.action, {
                method: 'POST',
                body: new FormData(form),
                headers: { 'Accept': 'application/json' }
            });
            if (res.ok) {
                form.reset();
                status.textContent = 'Thanks. You will hear from me when something cool happens.';
            } else {
                status.textContent = 'That did not go through. Email elvin@arbutus.audio instead.';
            }
        } catch (err) {
            status.textContent = 'That did not go through. Email elvin@arbutus.audio instead.';
        } finally {
            button.disabled = false;
        }
    });
}

document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.carousel').forEach(el => new Carousel(el));
    window.lightbox = new Lightbox();
    initSignup();

    document.addEventListener('keydown', (e) => {
        if (window.lightbox.isOpen()) {
            if (e.key === 'Escape') window.lightbox.close();
            if (e.key === 'ArrowLeft') window.lightbox.prev();
            if (e.key === 'ArrowRight') window.lightbox.next();
            return;
        }
        if (Carousel.hovered) {
            if (e.key === 'ArrowLeft') Carousel.hovered.prevSlide();
            if (e.key === 'ArrowRight') Carousel.hovered.nextSlide();
        }
    });
});
