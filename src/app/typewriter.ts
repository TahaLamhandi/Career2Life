import { Directive, ElementRef, Input, OnInit, OnDestroy } from '@angular/core';

@Directive({
  selector: '[appTypewriter]',
})
export class Typewriter implements OnInit, OnDestroy {
  @Input() appTypewriter: string = '';
  @Input() speed: number = 30; // milliseconds per character

  private observer: IntersectionObserver | null = null;
  private timeoutId: any;
  private currentIndex = 0;
  private isAnimating = false;
  private hasAnimated = false; // Flag to ensure animation runs only once

  constructor(private el: ElementRef) {}

  ngOnInit() {
    this.observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting && !this.isAnimating && !this.hasAnimated) {
            this.startTyping();
          }
        });
      },
      { threshold: 0.5 } // Trigger when 50% of the element is visible
    );

    this.observer.observe(this.el.nativeElement);
  }

  ngOnDestroy() {
    if (this.observer) {
      this.observer.disconnect();
    }
    if (this.timeoutId) {
      clearTimeout(this.timeoutId);
    }
  }

  private startTyping() {
    this.isAnimating = true;
    this.currentIndex = 0;
    this.el.nativeElement.textContent = '';
    this.typeNextCharacter();
  }

  private typeNextCharacter() {
    if (this.currentIndex < this.appTypewriter.length) {
      this.el.nativeElement.textContent += this.appTypewriter[this.currentIndex];
      this.currentIndex++;
      this.timeoutId = setTimeout(() => this.typeNextCharacter(), this.speed);
    } else {
      this.isAnimating = false;
      this.hasAnimated = true; // Mark as animated to prevent re-triggering
    }
  }
}
