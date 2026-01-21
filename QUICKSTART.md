# 🚀 Quick Start Guide

## Step 1: Install Python Dependencies

Open a terminal and run:
```bash
pip install -r requirements.txt
```

This will install:
- Flask (web framework)
- Flask-CORS (for API access from Angular)
- scikit-learn (machine learning)
- pandas (data processing)
- joblib (model loading)

## Step 2: Start the Flask API Server

In the same terminal, run:
```bash
python api.py
```

You should see:
```
==================================================
🚀 Career2Life API Server Starting...
==================================================
📍 Server running at: http://localhost:5000
📊 Available endpoints:
   - POST /predict-salary
   - POST /predict-car
   - POST /predict-house
==================================================
```

**Keep this terminal running!**

## Step 3: Start the Angular Development Server

Open a **NEW terminal** and run:
```bash
npm start
```

This will compile the Angular app and start the dev server. Once you see:
```
Application bundle generation complete. [X.XXXs]
Local: http://localhost:4200/
```

## Step 4: Open Your Browser

Navigate to: **http://localhost:4200/**

## 🎯 How to Use the App

1. **Home Page**: You'll see an animated journey map with three sections
   - Job Section: Click "Predict my salary"
   - Car Section: Click "Check car affordability"
   - House Section: Click "Estimate my future home"

2. **Salary Prediction Page**:
   - Fill in your age, gender, education level, job title, and years of experience
   - Click "Calculate Salary"
   - View your predicted salary!

3. **Car Affordability Page**:
   - Enter your annual salary, credit score, monthly debt, down payment, and loan term
   - Click "Check Affordability"
   - See if you can afford the car (green = yes, pink = stretch)
   - View maximum car price, monthly payment, and interest rate

4. **House Prediction Page**:
   - Fill in all the house details (bedrooms, bathrooms, square footage, etc.)
   - Click "Estimate Price"
   - Get an instant house price prediction!

## 🐛 Troubleshooting

### Port Already in Use
If port 5000 is already in use:
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### Python Packages Not Found
Make sure you're in the correct directory:
```bash
cd c:\Users\lamha\career2Life
pip install -r requirements.txt
```

### Angular Build Errors
Clear cache and reinstall:
```bash
rm -r node_modules
npm install
```

## ✅ Checklist

- [ ] Python dependencies installed
- [ ] Flask server running on port 5000
- [ ] Angular dev server running on port 4200
- [ ] Browser opened to http://localhost:4200/
- [ ] All three ML models (.pkl files) present in root directory

## 🎨 Features to Try

1. Navigate through the home page with smooth scrolling
2. Click on each prediction button
3. Fill out forms and see instant predictions
4. Click "Back" buttons to return to home
5. Try different values to see how predictions change!

---

**Enjoy your Career2Life journey! 🚀**
