import { Component, HostListener, ElementRef, ViewChild, AfterViewInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
    selector: 'app-journey-map',
    standalone: true,
    imports: [CommonModule],
    templateUrl: './journey-map.component.html',
    styleUrls: ['./journey-map.component.scss']
})
export class JourneyMapComponent implements AfterViewInit {
    @ViewChild('roadPath') roadPath!: ElementRef<SVGPathElement>;

    characterPosition = { x: 0, y: 0, angle: 0 };
    scrollPercentage = 0;

    // State tracking
    activeSection: 'home' | 'job' | 'car' | 'house' = 'home';
    hasSuit = false;
    hasCar = false;
    showWaitingCar = true;
    isTransitioning = false; // For smooth suit transformations
    showTooltip = false;

    // Section thresholds (approximate based on road path)
    private readonly JOB_THRESHOLD = 0.20;
    private readonly CAR_PICKUP_THRESHOLD = 0.62; // Pick up car at the first major curve peak (90, 250)
    private readonly HOUSE_ARRIVE_THRESHOLD = 0.96; // Optimized to park exactly at the house pin

    constructor() { }

    toggleTooltip(event?: Event) {
        if (event) event.stopPropagation();
        this.showTooltip = !this.showTooltip;

        // Play horn sound if we are in the car
        if (this.hasCar) {
            this.playHorn();
        }
    }

    private playHorn() {
        const audio = new Audio('car-horn.mp3');
        audio.volume = 0.4;
        audio.play().catch(err => console.error('Audio play failed:', err));
    }

    ngAfterViewInit() {
        // Use multiple attempts to ensure layout and SVG are ready
        this.initPosition();
        setTimeout(() => this.initPosition(), 100);
        setTimeout(() => this.initPosition(), 500);
    }

    private initPosition() {
        this.updateScrollPercentage();
        this.updateState();
        this.updateCharacterPosition();
    }

    @HostListener('window:scroll')
    onScroll() {
        this.initPosition();

        // Auto-hide tooltip on significant scroll
        if (this.scrollPercentage > 0.05) {
            this.showTooltip = false;
        }
    }

    @HostListener('window:resize')
    onResize() {
        this.updateCharacterPosition();
    }

    private updateScrollPercentage() {
        // Calculate scroll relative to the sections container specifically
        const sectionsContainer = document.querySelector('.sections-container');
        if (!sectionsContainer) return;

        const containerHeight = sectionsContainer.getBoundingClientRect().height;
        const scrollHeight = containerHeight - window.innerHeight;

        // Prevent division by zero or NaN
        if (scrollHeight <= 0) {
            this.scrollPercentage = 0;
            return;
        }

        const scrollTop = window.scrollY || document.documentElement.scrollTop;

        // Clamp between 0 and 1
        this.scrollPercentage = Math.max(0, Math.min(1, scrollTop / scrollHeight));
    }

    private updateCharacterPosition() {
        if (!this.roadPath) return;

        const path = this.roadPath.nativeElement;
        const pathLength = path.getTotalLength();

        // Start slightly down the road (3%) so the character is visible, and end at HOUSE_ARRIVE_THRESHOLD
        const startOffset = 0.03;
        const currentProgress = startOffset + (this.scrollPercentage * (this.HOUSE_ARRIVE_THRESHOLD - startOffset));
        const targetLength = pathLength * currentProgress;
        const point = path.getPointAtLength(targetLength);

        // Calculate angle
        const lookAhead = Math.min(pathLength, targetLength + 10);
        const pointAhead = path.getPointAtLength(lookAhead);
        // Add 90 degrees to align character forward
        const angle = (Math.atan2(pointAhead.y - point.y, pointAhead.x - point.x) * 180 / Math.PI);

        this.characterPosition = {
            x: point.x,
            y: point.y,
            angle: angle
        };
    }

    private updateState() {
        const previousHasSuit = this.hasSuit;

        // 1. Home -> Job (Suit Up)
        if (this.scrollPercentage < this.JOB_THRESHOLD) {
            this.activeSection = 'home';
            this.hasSuit = false;
            this.hasCar = false;
            this.showWaitingCar = true;
        }
        // 2. Job -> Car Pickup
        else if (this.scrollPercentage < this.CAR_PICKUP_THRESHOLD) {
            this.activeSection = 'job';
            this.hasSuit = true;
            this.hasCar = false;
            this.showWaitingCar = true;
        }
        // 3. Car Pickup -> Driving
        else {
            // User has reached the car
            this.activeSection = this.scrollPercentage < this.HOUSE_ARRIVE_THRESHOLD ? 'car' : 'house';
            this.hasSuit = true;
            this.hasCar = true; // Is now IN the car
            this.showWaitingCar = false; // Pickup happened
        }

        // Trigger transformation animation when suit state changes
        if (previousHasSuit !== this.hasSuit) {
            this.isTransitioning = true;
            setTimeout(() => {
                this.isTransitioning = false;
            }, 800); // Match CSS transition duration
        }
    }
}
