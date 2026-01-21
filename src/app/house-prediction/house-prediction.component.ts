import { Component, OnInit, AfterViewInit, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { ThemeService } from '../theme.service';

@Component({
  selector: 'app-house-prediction',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './house-prediction.component.html',
  styleUrls: ['./house-prediction.component.scss']
})
export class HousePredictionComponent implements OnInit, AfterViewInit {
  formData = {
    property_type: '',
    transaction: '',
    surface: '',
    rooms: '',
    bathrooms: '',
    floor: '',
    city: '',
    neighborhood: '',
    condition: '',
    age: ''
  };

  propertyTypes = ['Appartement', 'Duplex', 'Maison', 'Riad', 'Studio', 'Villa'];
  transactionTypes = ['Location', 'Location Vacances', 'Vente'];
  cities = ['Casablanca', 'Rabat', 'Marrakech', 'Fes', 'Tanger', 'Agadir', 'Meknes', 'Oujda', 'Kenitra', 'Tetouan', 'Sale'];
  conditions = ['A Renover', 'Bon Etat', 'Excellent Etat', 'Neuf', 'Tres Bon Etat'];

  prediction: number | null = null;
  isLoading = false;
  errorMessage = '';

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
      this.errorMessage = 'Please fill in all required fields';
      return;
    }

    this.isLoading = true;
    this.errorMessage = '';
    this.prediction = null;

    this.http.post<any>('http://localhost:5000/predict-house', this.formData)
      .subscribe({
        next: (response) => {
          this.prediction = response.predicted_price;
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
    return !!(
      this.formData.property_type && 
      this.formData.transaction && 
      this.formData.surface && 
      this.formData.rooms && 
      this.formData.bathrooms && 
      this.formData.floor && 
      this.formData.city && 
      this.formData.neighborhood && 
      this.formData.condition && 
      this.formData.age
    );
  }

  resetForm() {
    this.formData = {
      property_type: '',
      transaction: '',
      surface: '',
      rooms: '',
      bathrooms: '',
      floor: '',
      city: '',
      neighborhood: '',
      condition: '',
      age: ''
    };
    this.prediction = null;
    this.errorMessage = '';
  }
}
