import { Component, signal, HostListener, OnInit, OnDestroy } from '@angular/core';
import { JourneyMapComponent } from './journey-map/journey-map.component';
import { CommonModule } from '@angular/common';
import { Typewriter } from './typewriter';
import { SlideDownDirective } from './slide-down';
import Lenis from 'lenis';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [JourneyMapComponent, CommonModule, Typewriter, SlideDownDirective],
  templateUrl: './app.html',
  styleUrl: './app.scss'
})
export class App implements OnInit, OnDestroy {
  private lenis: Lenis | undefined;
  protected readonly title = signal('landing');
  logoSpanOffset = 0;   // For '2'
  logoSpanOffsetR = 0;  // For 'r'
  logoSpanOffsetL = 0;  // For 'L'
  isDarkMode = false;
  isMobileMenuOpen = false;

  scrollToSection(event: Event, sectionId: string) {
    event.preventDefault();
    this.closeMobileMenu();
    if (this.lenis) {
      this.lenis.scrollTo(sectionId, {
        duration: 1.2,
        easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
      });
    }
  }

  toggleMobileMenu() {
    this.isMobileMenuOpen = !this.isMobileMenuOpen;
  }

  closeMobileMenu() {
    this.isMobileMenuOpen = false;
  }

  toggleTheme() {
    this.isDarkMode = !this.isDarkMode;
    if (this.isDarkMode) {
      document.body.style.backgroundColor = '#121212';
      document.body.style.color = '#e0e0e0';
      
      // Make titles white
      const heroTitle = document.querySelector('.hero-title');
      if (heroTitle) (heroTitle as HTMLElement).style.color = '#fff';
      
      const sectionTitles = document.querySelectorAll('.section-title');
      sectionTitles.forEach(title => (title as HTMLElement).style.color = '#fff');
      
      // Make descriptions white
      const descriptions = document.querySelectorAll('.section-desc');
      descriptions.forEach(desc => (desc as HTMLElement).style.color = '#ccc');
      
      // Make footer white
      const footerLogo = document.querySelector('.footer-logo');
      if (footerLogo) (footerLogo as HTMLElement).style.color = '#fff';
      
      const footerSpans = document.querySelectorAll('.footer-logo-span');
      footerSpans.forEach(span => (span as HTMLElement).style.color = '#fff');
      
      const footerContent = document.querySelector('.footer-content');
      if (footerContent) (footerContent as HTMLElement).style.color = '#ccc';
      
      const footerNavLinks = document.querySelectorAll('.footer-nav a');
      footerNavLinks.forEach(link => (link as HTMLElement).style.color = '#ccc');
      
      // Make sections white
      const sections = document.querySelectorAll('.section');
      sections.forEach(section => (section as HTMLElement).style.color = '#e0e0e0');
      
      // Make nav pill dark
      const navPill = document.querySelector('.nav-pill');
      if (navPill) {
        (navPill as HTMLElement).style.backgroundColor = '#333';
        (navPill as HTMLElement).style.color = '#fff';
      }

      // Make buttons white with black text in dark mode
      const buttons = document.querySelectorAll('.cta');
      buttons.forEach(button => {
        (button as HTMLElement).style.backgroundColor = '#fff';
        (button as HTMLElement).style.color = '#000';
        (button as HTMLElement).style.border = '2px solid #fff';
      });

      // Update hover effects for dark mode
      const style = document.createElement('style');
      style.setAttribute('data-dark-mode-hover', 'true');
      style.textContent = `
        .cta:hover {
          background-color: #e0e0e0 !important;
          color: #000 !important;
        }
      `;
      document.head.appendChild(style);
    } else {
      document.body.style.backgroundColor = '';
      document.body.style.color = '';
      
      // Reset titles
      const heroTitle = document.querySelector('.hero-title');
      if (heroTitle) (heroTitle as HTMLElement).style.color = '';
      
      const sectionTitles = document.querySelectorAll('.section-title');
      sectionTitles.forEach(title => (title as HTMLElement).style.color = '');
      
      // Reset descriptions
      const descriptions = document.querySelectorAll('.section-desc');
      descriptions.forEach(desc => (desc as HTMLElement).style.color = '');
      
      // Reset footer
      const footerLogo = document.querySelector('.footer-logo');
      if (footerLogo) (footerLogo as HTMLElement).style.color = '';
      
      const footerSpans = document.querySelectorAll('.footer-logo-span');
      footerSpans.forEach(span => (span as HTMLElement).style.color = '');
      
      const footerContent = document.querySelector('.footer-content');
      if (footerContent) (footerContent as HTMLElement).style.color = '';
      
      const footerNavLinks = document.querySelectorAll('.footer-nav a');
      footerNavLinks.forEach(link => (link as HTMLElement).style.color = '');
      
      // Reset sections
      const sections = document.querySelectorAll('.section');
      sections.forEach(section => (section as HTMLElement).style.color = '');
      
      // Reset nav pill
      const navPill = document.querySelector('.nav-pill');
      if (navPill) {
        (navPill as HTMLElement).style.backgroundColor = '';
        (navPill as HTMLElement).style.color = '';
      }

      // Reset buttons to default
      const buttons = document.querySelectorAll('.cta');
      buttons.forEach(button => {
        (button as HTMLElement).style.backgroundColor = '';
        (button as HTMLElement).style.color = '';
        (button as HTMLElement).style.border = '';
      });

      // Remove dark mode hover styles
      const existingStyle = document.querySelector('style[data-dark-mode-hover]');
      if (existingStyle) {
        existingStyle.remove();
      }
    }
    console.log('Dark mode:', this.isDarkMode);
  }

  ngOnInit() {
    this.lenis = new Lenis({
      duration: 1.2,
      easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
      orientation: 'vertical',
      gestureOrientation: 'vertical',
      smoothWheel: true,
      wheelMultiplier: 1,
      touchMultiplier: 2,
    });

    // Scroll to home on refresh
    this.lenis.scrollTo('#home', { duration: 0 });

    const raf = (time: number) => {
      this.lenis?.raf(time);
      requestAnimationFrame(raf);
    }

    requestAnimationFrame(raf);
  }

  ngOnDestroy() {
    this.lenis?.destroy();
  }

  @HostListener('window:scroll')
  onScroll() {
    const scrollHeight = document.documentElement.scrollHeight - window.innerHeight;
    const scrollTop = window.scrollY || document.documentElement.scrollTop;
    const scrollPercentage = Math.max(0, Math.min(1, scrollTop / scrollHeight));

    // "2" Animation (Starts first at 98%)
    if (scrollPercentage > 0.98) {
      const progress = Math.min(1, (scrollPercentage - 0.98) / 0.015);
      this.logoSpanOffset = progress * -40;
    } else {
      this.logoSpanOffset = 0;
    }

    // "r" and "L" Animation (Starts slightly later at 98.5%)
    if (scrollPercentage > 0.985) {
      const progressStaggered = Math.min(1, (scrollPercentage - 0.985) / 0.01);
      this.logoSpanOffsetR = progressStaggered * -20; // Smaller jump for 'r'
      this.logoSpanOffsetL = progressStaggered * -20; // Smaller jump for 'L'
    } else {
      this.logoSpanOffsetR = 0;
      this.logoSpanOffsetL = 0;
    }
  }
}
