import { Component, OnInit, AfterViewInit, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { ThemeService } from '../theme.service';
import { timeout, catchError } from 'rxjs/operators';
import { throwError } from 'rxjs';
import { environment } from '../../environments/environment';

@Component({
  selector: 'app-salary-prediction',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './salary-prediction.component.html',
  styleUrls: ['./salary-prediction.component.scss']
})
export class SalaryPredictionComponent implements OnInit, AfterViewInit {
  formData = {
    job_title: '',
    skills: '',
    years_of_experience: '',
    location: '',
    education_level: ''
  };

  skillsList: string[] = [];
  currentSkill: string = '';
  prediction: number | null = null;
  isLoading = false;
  errorMessage = '';

  constructor(
    private router: Router,
    private http: HttpClient,
    public themeService: ThemeService,
    private cdr: ChangeDetectorRef
  ) {}

  ngOnInit() {
    this.themeService.initTheme();
  }

  ngAfterViewInit() {
    setTimeout(() => {
      window.scrollTo(0, 0);
    }, 0);
  }

  toggleTheme() {
    this.themeService.toggleTheme();
  }

  closeResult() {
    this.prediction = null;
  }

  educationLevels = [
    "Bachelor's",
    "Master's",
    "PhD"
  ];

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

    console.log('Sending data:', this.formData);

    this.http.post<any>(`${environment.apiUrl}/predict-salary`, this.formData)
      .pipe(
        timeout(10000),
        catchError((error: HttpErrorResponse) => {
          console.error('HTTP Error:', error);
          return throwError(() => error);
        })
      )
      .subscribe({
        next: (response) => {
          console.log('Received response:', response);
          this.prediction = response.predicted_salary;
          this.isLoading = false;
          console.log('Prediction set to:', this.prediction);
          console.log('isLoading set to:', this.isLoading);
          this.cdr.detectChanges();
          console.log('Change detection triggered');
        },
        error: (error) => {
          console.error('Error details:', error);
          this.errorMessage = `Failed to get prediction: ${error.message || 'Please try again'}`;
          this.isLoading = false;
          this.cdr.detectChanges();
        },
        complete: () => {
          console.log('Request completed');
        }
      });
  }

  addSkill(event: KeyboardEvent) {
    if (event.key === 'Enter') {
      event.preventDefault();
      const skill = this.currentSkill.trim();
      if (skill && !this.skillsList.includes(skill)) {
        this.skillsList.push(skill);
        this.formData.skills = this.skillsList.join(', ');
        this.currentSkill = '';
      }
    }
  }

  removeSkill(skill: string) {
    this.skillsList = this.skillsList.filter(s => s !== skill);
    this.formData.skills = this.skillsList.join(', ');
  }

  isFormValid(): boolean {
    return !!(this.formData.job_title && 
              this.formData.years_of_experience &&
              this.skillsList.length > 0 &&
              this.formData.location &&
              this.formData.education_level);
  }

  resetForm() {
    this.formData = {
      job_title: '',
      skills: '',
      years_of_experience: '',
      location: '',
      education_level: ''
    };
    this.skillsList = [];
    this.currentSkill = '';
    this.prediction = null;
    this.errorMessage = '';
  }
}
