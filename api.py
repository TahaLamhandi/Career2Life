from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the models
salary_model = None
car_model = None
house_model = None

try:
    salary_model = joblib.load('SalaryModel.pkl')
    print("✓ Salary model and encoder loaded successfully!")
except Exception as e:
    print(f"❌ Error loading salary model: {e}")

try:
    car_model = joblib.load('good_deal_model.pkl')
    print("✓ Car model loaded successfully!")
except Exception as e:
    print(f"⚠️ Error loading car model: {e}")

try:
    house_model = joblib.load('house_predictions.pkl')
    print("✓ House model loaded successfully!")
except Exception as e:
    print(f"⚠️ Error loading house model: {e}")

@app.route('/')
def home():
    return jsonify({
        'message': 'Career2Life API is running!',
        'endpoints': [
            '/predict-salary',
            '/predict-car',
            '/predict-house'
        ]
    })

@app.route('/predict-salary', methods=['POST'])
def predict_salary():
    try:
        data = request.json
        print(f"📥 Received salary data: {data}")
        
        # Parse skills
        skills_text = data.get('skills', '')
        if ',' in skills_text:
            skills_list = [s.strip() for s in skills_text.split(',') if s.strip()]
        else:
            skills_list = [s.strip() for s in skills_text.split() if s.strip()]
        
        skills_count = len(skills_list)
        tech_skills = ['python', 'java', 'javascript', 'react', 'angular', 'node', 'sql', 'mongodb', 'aws', 'docker', 'kubernetes']
        tech_skills_count = sum(1 for skill in skills_list if skill.lower() in tech_skills)
        
        # Parse experience
        experience_years = int(data['years_of_experience'])
        if experience_years < 1:
            experience_level = 'entry'
        elif experience_years < 2:
            experience_level = 'junior'
        elif experience_years < 5:
            experience_level = 'mid'
        elif experience_years < 10:
            experience_level = 'senior'
        else:
            experience_level = 'expert'
        
        # Parse education - match model's expected format
        education_map = {
            "Bachelor's": ("bachelor's degree", 1),
            "Master's": ("master's degree", 2),
            "PhD": ("phd", 3),
            "High School": ("diploma", 0)
        }
        education_info = education_map.get(data['education_level'], ("bachelor's degree", 1))
        education_required = education_info[0]
        education_level_numeric = education_info[1]
        
        # City tier (simple classification) - return as string
        location_lower = data['location'].lower()
        major_cities_tier1 = ['casablanca', 'rabat', 'marrakech']
        major_cities_tier2 = ['fes', 'tangier', 'agadir', 'meknes', 'oujda']
        
        if location_lower in major_cities_tier1:
            city_tier = 'tier1'
        elif location_lower in major_cities_tier2:
            city_tier = 'tier2'
        else:
            city_tier = 'tier3'
        
        # Create DataFrame with ALL required features
        input_data = pd.DataFrame([{
            'job_title': data['job_title'],
            'skills_required': skills_text,
            'experience_years': experience_years,
            'experience_level': experience_level,
            'education_required': education_required,
            'location': location_lower,
            'job_type': 'full-time',
            'skills_count': skills_count,
            'tech_skills_count': tech_skills_count,
            'experience_squared': experience_years ** 2,
            'edu_exp_interaction': education_level_numeric * experience_years,
            'city_tier': city_tier,
            'job_type_numeric': 1,
            'education_level_numeric': education_level_numeric
        }])
        
        # Explicit type conversion using astype
        categorical_cols = ['job_title', 'skills_required', 'experience_level', 'education_required', 'location', 'job_type', 'city_tier']
        numeric_cols = ['experience_years', 'skills_count', 'tech_skills_count', 'experience_squared', 'edu_exp_interaction', 'job_type_numeric', 'education_level_numeric']
        
        for col in categorical_cols:
            input_data[col] = input_data[col].astype(str)
        
        for col in numeric_cols:
            input_data[col] = input_data[col].astype('int64')
        
        print(f"📊 Salary input shape: {input_data.shape}")
        print(f"📋 Salary input columns: {input_data.columns.tolist()}")
        print(f"🔍 Data types:\n{input_data.dtypes}")
        print(f"🔍 Sample values:\n{input_data.iloc[0].to_dict()}")
        
        # Make prediction
        prediction = salary_model.predict(input_data)[0]
        print(f"💰 Salary prediction: {prediction}")
        
        return jsonify({
            'predicted_salary': float(prediction),
            'status': 'success'
        })
    
    except Exception as e:
        print(f"❌ Salary Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 400

@app.route('/predict-car', methods=['POST'])
def predict_car():
    try:
        data = request.json
        print(f"📥 Received car data: {data}")
        
        # Create DataFrame with the input data
        input_data = pd.DataFrame([{
            'model': data['model'],
            'year': int(data['year']),
            'km_driven': int(data['km_driven']),
            'fuel': data['fuel'],
            'condition': data['condition'],
            'first_owner': int(data['first_owner']),
            'fiscal_power': int(data['fiscal_power']),
            'price': float(data['price'])
        }])
        
        print(f"📊 Car input features shape: {input_data.shape}")
        print(f"📋 Car input features columns: {input_data.columns.tolist()}")
        print(f"🔍 Car input data:\n{input_data}")
        print(f"🔍 Car input data types:\n{input_data.dtypes}")
        
        # Make prediction with the model
        raw_prediction = car_model.predict(input_data)[0]
        print(f"🎯 Raw prediction value: {raw_prediction}")
        print(f"🎯 Raw prediction type: {type(raw_prediction)}")
        
        # Convert string prediction to boolean
        if isinstance(raw_prediction, str):
            is_good_deal = raw_prediction.lower() in ['yes', 'good', 'true', '1']
        else:
            is_good_deal = bool(raw_prediction)
        
        print(f"💰 Car prediction (is_good_deal): {is_good_deal}")
        
        return jsonify({
            'is_good_deal': is_good_deal,
            'status': 'success'
        })
    
    except Exception as e:
        print(f"❌ Car Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 400

@app.route('/predict-house', methods=['POST'])
def predict_house():
    try:
        data = request.json
        print(f"📥 Received house data: {data}")
        
        # Encode categorical features
        property_type_map = {'appartement': 0, 'duplex': 1, 'maison': 2, 'riad': 3, 'studio': 4, 'villa': 5}
        transaction_map = {'location': 0, 'location vacances': 1, 'vente': 2}
        city_map = {'casablanca': 0, 'rabat': 1, 'marrakech': 2, 'fes': 3, 'tanger': 4, 'agadir': 5, 
                   'meknes': 6, 'oujda': 7, 'kenitra': 8, 'tetouan': 9, 'sale': 10}
        condition_map = {'a renover': 0, 'bon etat': 1, 'excellent etat': 2, 'neuf': 3, 'tres bon etat': 4}
        
        # Create input array with 10 features
        # Order: property_type, transaction, surface, rooms, bathrooms, floor, city, neighborhood_encoded, condition, age
        neighborhood_encoded = hash(data.get('neighborhood', '')) % 100  # Simple encoding for neighborhood
        
        input_array = [[
            property_type_map.get(data['property_type'].lower(), 0),
            transaction_map.get(data['transaction'].lower(), 0),
            float(data['surface']),
            int(data['rooms']),
            int(data['bathrooms']),
            int(data['floor']),
            city_map.get(data['city'].lower(), 0),
            neighborhood_encoded,
            condition_map.get(data['condition'].lower(), 1),
            int(data['age'])
        ]]
        
        print(f"📊 House input array shape: {len(input_array)}x{len(input_array[0])}")
        print(f"🔍 House input values: {input_array[0]}")
        
        # Make prediction
        prediction = house_model.predict(input_array)[0]
        print(f"🏠 House prediction: {prediction:.2f} MAD")
        
        return jsonify({
            'predicted_price': float(prediction),
            'status': 'success'
        })
    
    except Exception as e:
        print(f"❌ House Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 400

if __name__ == '__main__':
    print("=" * 50)
    print("🚀 Career2Life API Server Starting...")
    print("=" * 50)
    print("📍 Server running at: http://localhost:5000")
    print("📊 Available endpoints:")
    print("   - POST /predict-salary")
    print("   - POST /predict-car")
    print("   - POST /predict-house")
    print("=" * 50)
    app.run(debug=True, port=5000)
