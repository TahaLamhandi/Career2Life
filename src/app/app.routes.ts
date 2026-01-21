import { Routes } from '@angular/router';
import { SalaryPredictionComponent } from './salary-prediction/salary-prediction.component';
import { CarAffordabilityComponent } from './car-affordability/car-affordability.component';
import { HousePredictionComponent } from './house-prediction/house-prediction.component';
import { App } from './app';

export const routes: Routes = [
  { path: '', component: App },
  { path: 'salary-prediction', component: SalaryPredictionComponent },
  { path: 'car-affordability', component: CarAffordabilityComponent },
  { path: 'house-prediction', component: HousePredictionComponent }
];
