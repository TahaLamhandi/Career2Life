import { Injectable, signal } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ThemeService {
  isDarkMode = signal(false);

  toggleTheme() {
    this.isDarkMode.update(value => !value);
    // Also set body style so home page can detect it
    if (this.isDarkMode()) {
      document.body.style.backgroundColor = 'rgb(18, 18, 18)';
    } else {
      document.body.style.backgroundColor = '';
    }
  }

  initTheme() {
    // Sync with body background
    const isDark = document.body.style.backgroundColor === 'rgb(18, 18, 18)';
    this.isDarkMode.set(isDark);
  }
}
