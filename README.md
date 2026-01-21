# Career2Life - Your Career Journey Planner

A beautiful, interactive web application that helps you predict your career salary, check car affordability, and estimate house prices using machine learning models.

🌐 **[Live Demo](https://career2life.vercel.app)** | 📚 **[Deployment Guide](DEPLOYMENT_GUIDE.md)**

## ✨ Features

- 🎯 **Salary Prediction**: Predict your potential salary based on age, education, job title, and experience
- 🚗 **Car Affordability Check**: Determine if you can afford your dream car based on your finances
- 🏡 **House Price Estimation**: Estimate the value of your future home based on various property features
- 🎨 **Beautiful UI**: Modern, animated interface with smooth transitions and responsive design
- 🛣️ **Interactive Journey Map**: Visual representation of your career journey

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Career2Life.git
   cd Career2Life
   ```

2. **Install Frontend Dependencies**
   ```bash
   npm install
   ```

3. **Install Python Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the Backend (Terminal 1)**
   ```bash
   python api.py
   ```

5. **Start the Frontend (Terminal 2)**
   ```bash
   npm start
   ```

6. **Open your browser**
   Navigate to `http://localhost:4200`

## 🌐 Deployment

See the detailed [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for step-by-step instructions on deploying to:
- **Vercel** (Frontend - Free)
- **Render** (Backend API - Free)

Quick deployment steps:
1. Push your code to GitHub
2. Deploy backend to Render
3. Update `environment.prod.ts` with your Render API URL
4. Deploy frontend to Vercel

## 📁 Project Structure

```
Career2Life/
├── src/                          # Angular frontend source
│   ├── app/                      # Angular components
│   │   ├── salary-prediction/    # Salary prediction feature
│   │   ├── car-affordability/    # Car affordability checker
│   │   ├── house-prediction/     # House price estimator
│   │   └── ...
│   └── environments/             # Environment configurations
├── api.py                        # Flask backend API
├── *.pkl                         # Trained ML models
├── requirements.txt              # Python dependencies
├── package.json                  # Node dependencies
├── vercel.json                   # Vercel configuration
└── render.yaml                   # Render configuration
```

## 🛠️ Technologies

### Frontend
- Angular 21
- TypeScript
- SCSS
- RxJS

### Backend
- Flask (Python)
- scikit-learn
- pandas
- joblib

### Deployment
- Vercel (Frontend hosting)
- Render (Backend API hosting)

## 📦 Prerequisites

- Node.js (v18 or higher)
- Python 3.8+
- npm

### Installation

1. **Install Frontend Dependencies**
   ```bash
   npm install
   ```

2. **Install Python Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🏃 Running the Application

You need to run both the frontend (Angular) and backend (Flask) servers:

### 1. Start the Flask API Server

In one terminal:
```bash
python api.py
```

The API will be available at `http://localhost:5000`

### 2. Start the Angular Development Server

In another terminal:
```bash
npm start
```

The app will be available at `http://localhost:4200`

## 📊 API Endpoints

### POST `/predict-salary`
Predicts salary based on user credentials.

**Request Body:**
```json
{
  "age": 30,
  "gender": "Male",
  "education_level": "Bachelor's",
  "job_title": "Software Engineer",
  "years_of_experience": 5
}
```

### POST `/predict-car`
Determines car affordability.

**Request Body:**
```json
{
  "annual_salary": 75000,
  "credit_score": 720,
  "monthly_debt": 500,
  "down_payment": 10000,
  "loan_term": 60
}
```

### POST `/predict-house`
Estimates house price.

**Request Body:**
```json
{
  "bedrooms": 3,
  "bathrooms": 2,
  "sqft_living": 2000,
  "sqft_lot": 5000,
  "floors": 2,
  "waterfront": 0,
  "view": 2,
  "condition": 4,
  "grade": 8,
  "sqft_above": 1800,
  "sqft_basement": 200,
  "yr_built": 2010,
  "yr_renovated": 0
}
```

## 🎨 Pages

1. **Home Page** (`/`) - Interactive journey with navigation to all features
2. **Salary Prediction** (`/salary-prediction`) - Form to predict your future salary
3. **Car Affordability** (`/car-affordability`) - Check if you can afford a car
4. **House Prediction** (`/house-prediction`) - Estimate house prices

## 🛠️ Technologies Used

### Frontend
- Angular 21
- TypeScript
- SCSS
- Lenis (Smooth Scrolling)
- RxJS

### Backend
- Flask
- Flask-CORS
- scikit-learn
- pandas
- joblib

## 📁 Project Structure

```
career2Life/
├── src/
│   ├── app/
│   │   ├── salary-prediction/     # Salary prediction page
│   │   ├── car-affordability/     # Car affordability page
│   │   ├── house-prediction/      # House price prediction page
│   │   ├── journey-map/           # Interactive journey visualization
│   │   └── ...
│   ├── index.html
│   └── main.ts
├── api.py                         # Flask API server
├── salary_model.pkl              # ML model for salary prediction
├── good_deal_model.pkl           # ML model for car affordability
├── house_predictions.pkl         # ML model for house prices
├── requirements.txt              # Python dependencies
└── package.json                  # Node dependencies
```

## 🎯 ML Models

The application uses three pre-trained machine learning models:
- **salary_model.pkl**: Predicts salary based on career attributes
- **good_deal_model.pkl**: Determines car purchase affordability
- **house_predictions.pkl**: Estimates house prices based on property features

## 🌟 Features in Detail

### Salary Prediction
- Enter your age, gender, education level, job title, and experience
- Get instant salary predictions
- Beautiful gradient design with smooth animations

### Car Affordability
- Input your financial details
- Get maximum affordable car price
- View estimated monthly payments and interest rates
- Color-coded results (green for affordable, pink for stretch)

### House Price Estimation
- Comprehensive property details form
- Instant price estimation
- User-friendly interface with emoji icons

## 🤝 Contributing

Feel free to fork this project and submit pull requests!

## 📄 License

This project is licensed under the MIT License.

## 🎨 Design Philosophy

The application follows a modern design approach with:
- Smooth animations and transitions
- Gradient backgrounds
- Responsive layouts
- Accessible forms with clear labels
- Glass-morphism effects

---

**Developed with ❤️ for Career2Life**
