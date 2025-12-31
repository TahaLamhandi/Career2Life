import { Directive, ElementRef, OnInit, OnDestroy, Renderer2 } from '@angular/core';

@Directive({
  selector: '[appSlideDown]',
})
export class SlideDownDirective implements OnInit, OnDestroy {
  private observer: IntersectionObserver | null = null;
  private hasAnimated = false;

  constructor(private el: ElementRef, private renderer: Renderer2) {}

  ngOnInit() {
    // Initially hide the element
    this.renderer.setStyle(this.el.nativeElement, 'transform', 'translateY(-20px)');
    this.renderer.setStyle(this.el.nativeElement, 'opacity', '0');
    this.renderer.setStyle(this.el.nativeElement, 'transition', 'transform 2s ease-in-out, opacity 2s ease-in-out');

    this.observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting && !this.hasAnimated) {
            this.hasAnimated = true;
            // Trigger the slide down
            this.renderer.setStyle(this.el.nativeElement, 'transform', 'translateY(0)');
            this.renderer.setStyle(this.el.nativeElement, 'opacity', '1');
          }
        });
      },
      { threshold: 0.5 }
    );

    this.observer.observe(this.el.nativeElement);
  }

  ngOnDestroy() {
    if (this.observer) {
      this.observer.disconnect();
    }
  }
}