import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.preprocessing import LabelEncoder
import re
import joblib

# Load the dataset
df = pd.read_csv('morocco_jobs_dataset.csv')

# Function to parse salary
def parse_salary(salary_str):
    match = re.search(r'(\d+) MAD/month', salary_str)
    if match:
        return int(match.group(1))
    return None

# Function to parse experience
def parse_experience(exp_str):
    if pd.isna(exp_str):
        return 0
    match = re.search(r'(\d+)-(\d+) years', exp_str)
    if match:
        min_exp = int(match.group(1))
        max_exp = int(match.group(2))
        return (min_exp + max_exp) / 2
    match = re.search(r'(\d+)\+ years', exp_str)
    if match:
        return int(match.group(1)) + 2  # approximate
    match = re.search(r'(\d+)-(\d+) years', exp_str)  # wait, already have
    return 0

# Apply parsing
df['salary'] = df['salary'].apply(parse_salary)
df['experience_years'] = df['experience_required'].apply(parse_experience)
df['num_skills'] = df['skills_required'].apply(lambda x: len(x.split(', ')) if pd.notna(x) else 0)

# Drop rows with missing salary
df = df.dropna(subset=['salary'])

# Encode job_title
le = LabelEncoder()
df['job_title_encoded'] = le.fit_transform(df['job_title'])

# Features
X = df[['job_title_encoded', 'num_skills', 'experience_years']]
y = df['salary']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Absolute Error: {mae}")
print(f"Mean Squared Error: {mse}")

# Save model and encoder
joblib.dump(model, 'SalaryModel.pkl')
joblib.dump(le, 'job_title_encoder.pkl')
print("Model and encoder saved successfully!")
print(f"Model saved to: SalaryModel.pkl")
print(f"Encoder saved to: job_title_encoder.pkl")