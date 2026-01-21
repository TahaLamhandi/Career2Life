"""
Morocco Jobs Salary Prediction - Realistic & Logical Model
This model properly values:
1. High-value skills (AI/ML/Cloud) over skill quantity
2. Experience (0 years vs 10 years should have MASSIVE difference)
3. Input validation (no negative experience)
"""

import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv('morocco_jobs_dataset.csv')

# Parse salary
df['salary_numeric'] = df['salary'].str.replace(' MAD/month', '').str.replace(',', '').astype(int)

print("📊 Dataset Statistics:")
print(f"Total jobs: {len(df):,}")
print(f"Salary range: {df['salary_numeric'].min():,} - {df['salary_numeric'].max():,} MAD/month")
print(f"Average: {df['salary_numeric'].mean():,.0f} MAD/month\n")

# Define high-value skills with weights
HIGH_VALUE_SKILLS = {
    # AI/ML/Data Science - HIGHEST VALUE
    'Machine Learning': 1.0,
    'Deep Learning': 1.0,
    'AI': 1.0,
    'TensorFlow': 0.9,
    'PyTorch': 0.9,
    'NLP': 0.9,
    'Data Science': 0.85,
    'Big Data': 0.8,
    'Spark': 0.8,
    'Hadoop': 0.75,
    
    # Cloud & DevOps - VERY HIGH VALUE  
    'AWS': 0.9,
    'Azure': 0.9,
    'GCP': 0.9,
    'Kubernetes': 0.85,
    'Docker': 0.8,
    'Terraform': 0.8,
    'CI/CD': 0.75,
    'Jenkins': 0.7,
    
    # Programming Languages - HIGH VALUE
    'Python': 0.75,
    'Java': 0.7,
    'JavaScript': 0.65,
    'TypeScript': 0.7,
    'Go': 0.8,
    'Rust': 0.85,
    'Scala': 0.8,
    'C++': 0.7,
    
    # Backend/Databases - GOOD VALUE
    'Node.js': 0.65,
    'PostgreSQL': 0.6,
    'MongoDB': 0.65,
    'Redis': 0.6,
    'Microservices': 0.7,
    'REST API': 0.5,
    'GraphQL': 0.65,
    
    # Frontend - MODERATE VALUE
    'React': 0.6,
    'Angular': 0.6,
    'Vue.js': 0.6,
    
    # Mobile - MODERATE VALUE
    'iOS': 0.65,
    'Android': 0.65,
    'Flutter': 0.7,
    'React Native': 0.7,
    'Swift': 0.65,
    'Kotlin': 0.65,
    
    # Other Technical
    'Blockchain': 0.85,
    'Cybersecurity': 0.8,
    'Penetration Testing': 0.8,
}

def calculate_skill_score(skills_str):
    """
    Calculate weighted skill score - QUALITY matters more than quantity!
    Returns: (total_score, high_value_count, skill_details)
    """
    if pd.isna(skills_str) or skills_str.strip() == '':
        return 0, 0, ""
    
    skills_lower = skills_str.lower()
    total_score = 0
    high_value_count = 0
    matched_skills = []
    
    for skill, weight in HIGH_VALUE_SKILLS.items():
        if skill.lower() in skills_lower:
            total_score += weight
            high_value_count += 1
            matched_skills.append(f"{skill}({weight})")
    
    return total_score, high_value_count, ", ".join(matched_skills)

def get_seniority_multiplier(job_title):
    """Get salary multiplier based on seniority"""
    title_lower = job_title.lower()
    if 'principal' in title_lower or 'lead' in title_lower:
        return 1.8
    elif 'staff' in title_lower:
        return 1.6
    elif 'senior' in title_lower or 'sr' in title_lower:
        return 1.3
    elif 'junior' in title_lower or 'jr' in title_lower:
        return 0.7
    else:
        return 1.0  # Mid-level

def predict_salary_realistic(
    job_title,
    location,
    education,
    experience_years,
    job_type,
    skills_list
):
    """
    Predict salary with REALISTIC logic:
    - High-value skills dominate
    - Experience has major impact
    - 0 experience = much lower salary
    - Input validation
    """
    
    # ===== INPUT VALIDATION =====
    if not skills_list or len(skills_list) == 0:
        return "❌ ERROR: Skills are required! Cannot predict without skills."
    
    if experience_years < 0:
        return "❌ ERROR: Experience cannot be negative! Please enter 0 or positive number."
    
    if experience_years > 50:
        return "⚠️ WARNING: Experience seems too high. Maximum considered is 50 years."
    
    # ===== CALCULATE SKILL SCORE (MOST IMPORTANT!) =====
    skills_str = ', '.join(skills_list)
    skill_score, high_value_count, skill_details = calculate_skill_score(skills_str)
    
    if skill_score == 0:
        return f"⚠️ LOW VALUE SKILLS: Your skills don't include high-value technical skills. Expected salary: 5,000-8,000 MAD/month for entry-level positions."
    
    # ===== BASE SALARY FROM JOB ROLE =====
    job_lower = job_title.lower()
    
    # Determine base salary by role type
    if 'ai' in job_lower or 'machine learning' in job_lower or 'ml' in job_lower:
        base_salary = 25000  # AI/ML roles start high
    elif 'data scientist' in job_lower:
        base_salary = 23000
    elif 'devops' in job_lower or 'cloud' in job_lower:
        base_salary = 22000
    elif 'full stack' in job_lower:
        base_salary = 18000
    elif 'backend' in job_lower or 'software' in job_lower:
        base_salary = 17000
    elif 'frontend' in job_lower or 'mobile' in job_lower:
        base_salary = 15000
    elif 'data' in job_lower or 'analyst' in job_lower:
        base_salary = 14000
    elif 'qa' in job_lower or 'test' in job_lower:
        base_salary = 12000
    elif 'engineer' in job_lower:
        base_salary = 16000
    else:
        base_salary = 12000
    
    # ===== SENIORITY MULTIPLIER =====
    seniority_mult = get_seniority_multiplier(job_title)
    
    # ===== EXPERIENCE MULTIPLIER (HUGE IMPACT!) =====
    if experience_years == 0:
        exp_mult = 0.6  # 40% reduction for no experience
    elif experience_years <= 1:
        exp_mult = 0.75
    elif experience_years <= 2:
        exp_mult = 0.9
    elif experience_years <= 3:
        exp_mult = 1.0
    elif experience_years <= 5:
        exp_mult = 1.2
    elif experience_years <= 7:
        exp_mult = 1.5
    elif experience_years <= 10:
        exp_mult = 1.8
    elif experience_years <= 15:
        exp_mult = 2.2
    else:
        exp_mult = 2.5  # 15+ years = 2.5x multiplier
    
    # ===== SKILL QUALITY MULTIPLIER (QUALITY > QUANTITY!) =====
    # This is KEY: high-value skills should multiply salary significantly
    skill_mult = 1.0 + (skill_score * 0.15)  # Each skill point adds 15%
    
    # Bonus for many high-value skills
    if high_value_count >= 6:
        skill_mult *= 1.3  # 30% bonus for 6+ premium skills
    elif high_value_count >= 4:
        skill_mult *= 1.15  # 15% bonus for 4-5 premium skills
    
    # ===== EDUCATION MULTIPLIER =====
    if education == 'PhD':
        edu_mult = 1.35
    elif education == "Master's Degree":
        edu_mult = 1.20
    elif education == "Bachelor's Degree":
        edu_mult = 1.0
    else:
        edu_mult = 0.85
    
    # ===== LOCATION MULTIPLIER =====
    location_mult = {
        'Casablanca': 1.18,
        'Rabat': 1.15,
        'Tangier': 1.08,
        'Marrakech': 1.08,
        'Mohammedia': 1.10,
    }.get(location, 1.0)
    
    # ===== JOB TYPE MULTIPLIER =====
    type_mult = {
        'Full-time': 1.0,
        'Contract': 1.15,
        'Part-time': 0.65,
        'Internship': 0.50
    }.get(job_type, 1.0)
    
    # ===== FINAL CALCULATION =====
    predicted_salary = (
        base_salary * 
        seniority_mult * 
        exp_mult * 
        skill_mult * 
        edu_mult * 
        location_mult * 
        type_mult
    )
    
    # Round to nearest 100
    predicted_salary = round(predicted_salary / 100) * 100
    
    # Apply realistic bounds
    if predicted_salary < 4000:
        predicted_salary = 4000
    elif predicted_salary > 120000:
        predicted_salary = 120000
    
    # Return detailed result
    result = {
        'salary': int(predicted_salary),
        'breakdown': {
            'base_salary': base_salary,
            'seniority_mult': f"{seniority_mult}x",
            'experience_mult': f"{exp_mult}x",
            'skill_mult': f"{skill_mult:.2f}x",
            'education_mult': f"{edu_mult}x",
            'location_mult': f"{location_mult}x",
            'job_type_mult': f"{type_mult}x"
        },
        'skill_analysis': {
            'skill_score': f"{skill_score:.2f}",
            'high_value_count': high_value_count,
            'matched_skills': skill_details
        }
    }
    
    return result


# ===== TEST CASES =====
print("\n" + "="*80)
print("🧪 TEST CASE 1: Junior AI Engineer (0 experience)")
print("="*80)
result1 = predict_salary_realistic(
    job_title='AI Engineer',
    location='Casablanca',
    education="Master's Degree",
    experience_years=0,
    job_type='Full-time',
    skills_list=['Python', 'Machine Learning']
)
if isinstance(result1, dict):
    print(f"💰 Predicted Salary: {result1['salary']:,} MAD/month")
    print(f"\n📊 Breakdown:")
    for key, val in result1['breakdown'].items():
        print(f"   {key}: {val}")
    print(f"\n🎯 Skills Analysis:")
    print(f"   Score: {result1['skill_analysis']['skill_score']}")
    print(f"   High-value skills: {result1['skill_analysis']['high_value_count']}")
else:
    print(result1)

print("\n" + "="*80)
print("🧪 TEST CASE 2: Senior AI Engineer (10 years, many premium skills)")
print("="*80)
result2 = predict_salary_realistic(
    job_title='Senior AI Engineer',
    location='Casablanca',
    education="Master's Degree",
    experience_years=10,
    job_type='Full-time',
    skills_list=['Python', 'Machine Learning', 'TensorFlow', 'Deep Learning', 'AWS', 'Docker', 'Kubernetes']
)
if isinstance(result2, dict):
    print(f"💰 Predicted Salary: {result2['salary']:,} MAD/month")
    print(f"💡 That's {result2['salary'] - result1['salary']:,} MAD more than 0 experience!")
    print(f"\n📊 Breakdown:")
    for key, val in result2['breakdown'].items():
        print(f"   {key}: {val}")
    print(f"\n🎯 Skills Analysis:")
    print(f"   Score: {result2['skill_analysis']['skill_score']}")
    print(f"   High-value skills: {result2['skill_analysis']['high_value_count']}")
    print(f"   Matched: {result2['skill_analysis']['matched_skills']}")
else:
    print(result2)

print("\n" + "="*80)
print("🧪 TEST CASE 3: Your Example (AI Engineer, 0 years, 7 high-value skills)")
print("="*80)
result3 = predict_salary_realistic(
    job_title='AI Engineer',
    location='Casablanca',
    education="Master's Degree",
    experience_years=0,
    job_type='Full-time',
    skills_list=['C', 'Linux', 'Laravel', 'Java', 'IoT', 'Machine Learning', 'React', 'Node.js', 'Python', 'Docker', 'AWS', 'PostgreSQL']
)
if isinstance(result3, dict):
    print(f"💰 Predicted Salary: {result3['salary']:,} MAD/month")
    print(f"💡 Even with 0 experience, many premium skills boost salary!")
    print(f"\n📊 Breakdown:")
    for key, val in result3['breakdown'].items():
        print(f"   {key}: {val}")
    print(f"\n🎯 Skills Analysis:")
    print(f"   Score: {result3['skill_analysis']['skill_score']}")
    print(f"   High-value skills: {result3['skill_analysis']['high_value_count']}")
else:
    print(result3)

print("\n" + "="*80)
print("🧪 TEST CASE 4: Same skills but 10 years experience")
print("="*80)
result4 = predict_salary_realistic(
    job_title='Senior AI Engineer',
    location='Casablanca',
    education="Master's Degree",
    experience_years=10,
    job_type='Full-time',
    skills_list=['C', 'Linux', 'Laravel', 'Java', 'IoT', 'Machine Learning', 'React', 'Node.js', 'Python', 'Docker', 'AWS', 'PostgreSQL']
)
if isinstance(result4, dict):
    print(f"💰 Predicted Salary: {result4['salary']:,} MAD/month")
    print(f"💡 Experience boost: +{result4['salary'] - result3['salary']:,} MAD ({((result4['salary']/result3['salary'])-1)*100:.0f}% increase!)")
    print(f"\n📊 Breakdown:")
    for key, val in result4['breakdown'].items():
        print(f"   {key}: {val}")
else:
    print(result4)

print("\n" + "="*80)
print("🧪 TEST CASE 5: Negative experience (should fail)")
print("="*80)
result5 = predict_salary_realistic(
    job_title='Software Engineer',
    location='Rabat',
    education="Bachelor's Degree",
    experience_years=-2,
    job_type='Full-time',
    skills_list=['Python', 'Java']
)
print(result5)

print("\n" + "="*80)
print("🧪 TEST CASE 6: No high-value skills")
print("="*80)
result6 = predict_salary_realistic(
    job_title='Web Developer',
    location='Rabat',
    education="Bachelor's Degree",
    experience_years=3,
    job_type='Full-time',
    skills_list=['HTML', 'CSS', 'Bootstrap', 'jQuery']
)
print(result6)

print("\n" + "="*80)
print("✅ Model is now REALISTIC and LOGICAL!")
print("="*80)
print("\n🎯 Key Improvements:")
print("1. ✅ High-value skills (AI/ML/Cloud) have MASSIVE impact")
print("2. ✅ Experience 0→10 years = 200-300% salary increase")
print("3. ✅ Input validation (no negative experience)")
print("4. ✅ Skill QUALITY matters more than quantity")
print("5. ✅ Realistic salary ranges (4k - 120k MAD)")
