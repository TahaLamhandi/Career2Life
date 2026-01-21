import { Component, OnInit, AfterViewInit, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { ThemeService } from '../theme.service';

@Component({
  selector: 'app-car-affordability',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './car-affordability.component.html',
  styleUrls: ['./car-affordability.component.scss']
})
export class CarAffordabilityComponent implements OnInit, AfterViewInit {
  formData = {
    model: '',
    year: '',
    km_driven: '',
    fuel: '',
    condition: '',
    first_owner: '1',
    fiscal_power: '',
    price: ''
  };

  prediction: any = null;
  isLoading = false;
  errorMessage = '';

  fuelTypes = ['Diesel', 'Essence', 'Electric', 'Hybrid'];
  conditionLevels = ['Excellent', 'Good', 'Fair', 'Poor'];

  constructor(
    private router: Router,
    private http: HttpClient,
    public themeService: ThemeService,
    private cdr: ChangeDetectorRef
  ) {}

  toggleTheme() {
    this.themeService.toggleTheme();
  }

  closeResult() {
    this.prediction = null;
  }

  ngOnInit() {
    this.themeService.initTheme();
  }

  ngAfterViewInit() {
    setTimeout(() => {
      window.scrollTo(0, 0);
    }, 0);
  }

  goBack() {
    this.router.navigate(['/']);
  }

  onSubmit() {
    if (!this.isFormValid()) {
      this.errorMessage = 'Please fill in all fields';
      return;
    }

    this.isLoading = true;
    this.errorMessage = '';
    this.prediction = null;

    this.http.post<any>('http://localhost:5000/predict-car', this.formData)
      .subscribe({
        next: (response) => {
          this.prediction = response;
          this.isLoading = false;
          this.cdr.detectChanges();
        },
        error: (error) => {
          this.errorMessage = 'Failed to get prediction. Please try again.';
          this.isLoading = false;
          this.cdr.detectChanges();
          console.error('Error:', error);
        }
      });
  }

  isFormValid(): boolean {
    return !!(this.formData.model && 
              this.formData.year && 
              this.formData.km_driven && 
              this.formData.fuel &&
              this.formData.condition &&
              this.formData.first_owner &&
              this.formData.fiscal_power &&
              this.formData.price);
  }

  resetForm() {
    this.formData = {
      model: '',
      year: '',
      km_driven: '',
      fuel: '',
      condition: '',
      first_owner: '1',
      fiscal_power: '',
      price: ''
    };
    this.prediction = null;
    this.errorMessage = '';
  }

  getAffordabilityClass(): string {
    if (!this.prediction) return '';
    return this.prediction.is_good_deal ? 'affordable' : 'stretch';
  }

  getAffordabilityMessage(): string {
    if (!this.prediction) return '';
    return this.prediction.is_good_deal 
      ? '✓ Great! This is a good deal' 
      : '⚠ This might not be the best deal';
  }
}
