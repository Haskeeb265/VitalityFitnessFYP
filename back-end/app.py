from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

# Initialize Flask app
app = Flask(__name__)

# Configure Gemini API
GEMINI_API_KEY = 'AIzaSyCW6_wS5e3FoT2VOGkAYF6I3O-jJzLoF6A'
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# Helper functions for exercise safety and recommendations
def validate_medical_safety(medical_condition):
    safety_guidelines = {
        'none': [
            "Always warm up before exercising",
            "Stay hydrated during workouts",
            "Use proper form for all exercises",
            "Stop if you experience unusual pain or discomfort"
        ],
        'HyperTension': [
            "Monitor blood pressure before and after exercise",
            "Avoid holding breath during exercises",
            "Keep intensity moderate",
            "Avoid sudden position changes",
            "Take regular breaks during workouts",
            "Stop if experiencing dizziness or severe headache"
        ],
        'Coronary Heart Disease': [
            "Monitor heart rate continuously",
            "Start with low-intensity exercises",
            "Avoid exercises that cause chest pain",
            "Take frequent breaks",
            "Keep nitroglycerin nearby if prescribed",
            "Stop immediately if experiencing chest pain or shortness of breath"
        ],
        'Atrial Fibrillation': [
            "Monitor pulse rate and rhythm",
            "Avoid high-intensity exercises",
            "Take breaks as needed",
            "Stay well-hydrated",
            "Stop if heart rhythm feels irregular"
        ],
        'Asthma': [
            "Keep inhaler nearby during exercise",
            "Warm up thoroughly",
            "Avoid exercising in cold or dry air",
            "Monitor breathing patterns",
            "Stop if experiencing wheezing or severe shortness of breath"
        ],
        'Chronic obstructive pulmonary disease': [
            "Use pursed lip breathing technique",
            "Start with short exercise sessions",
            "Keep emergency inhaler nearby",
            "Focus on breathing exercises",
            "Stop if experiencing severe breathlessness"
        ],
        'Sleep Apnea': [
            "Avoid exercises that strain neck muscles",
            "Keep intensity moderate",
            "Focus on weight loss exercises if overweight",
            "Avoid exercising close to bedtime"
        ],
        'Type 1 Diabetes': [
            "Check blood sugar before, during, and after exercise",
            "Keep fast-acting sugar source nearby",
            "Stay well-hydrated",
            "Monitor for signs of hypoglycemia",
            "Wear medical ID bracelet during exercise"
        ],
        'Type 2 Diabetes': [
            "Check blood sugar before and after exercise",
            "Start with low-intensity exercises",
            "Keep sugar source nearby",
            "Stay hydrated",
            "Monitor for signs of low blood sugar"
        ],
        'Hypothyroidism': [
            "Start with low-intensity exercises",
            "Increase intensity gradually",
            "Focus on joint-friendly exercises",
            "Monitor heart rate",
            "Take longer rest periods if needed"
        ],
        'Hyperthyroidism': [
            "Avoid high-intensity exercises",
            "Monitor heart rate closely",
            "Stay well-hydrated",
            "Take frequent breaks",
            "Stop if experiencing rapid heartbeat or excessive sweating"
        ],
        'Polycystic Ovary Syndrome': [
            "Focus on regular, moderate exercise",
            "Include both cardio and strength training",
            "Stay hydrated",
            "Monitor intensity levels",
            "Take breaks as needed"
        ],
        'Osteoarthritis': [
            "Focus on low-impact exercises",
            "Avoid exercises that cause joint pain",
            "Use proper form",
            "Apply ice after exercise if needed",
            "Stop if experiencing increased joint pain"
        ],
        'Rheumatoid Arthritis': [
            "Exercise during periods of low disease activity",
            "Start with gentle movements",
            "Avoid high-impact exercises",
            "Use heat therapy before exercise if helpful",
            "Stop if experiencing increased joint pain or swelling"
        ],
        'Carpal Tunnel Syndrome': [
            "Avoid exercises that strain wrists",
            "Use proper form and grip",
            "Take frequent breaks",
            "Wear wrist support if recommended",
            "Stop if experiencing increased numbness or pain"
        ],
        'Osteoporosis': [
            "Avoid high-impact exercises",
            "Focus on balance and stability",
            "Avoid exercises with twisting motions",
            "Use proper form",
            "Stop if experiencing any sharp pain"
        ],
        'Multiple Sclerosis': [
            "Exercise in cool environments",
            "Take frequent breaks",
            "Stay hydrated",
            "Monitor fatigue levels",
            "Stop if experiencing increased symptoms or excessive fatigue"
        ],
        'other': [
            "Consult with healthcare provider before starting",
            "Start with low-intensity exercises",
            "Monitor symptoms closely",
            "Keep exercise sessions short initially",
            "Stop if experiencing unusual symptoms"
        ]
    }
    return safety_guidelines.get(medical_condition, ["Consult with healthcare provider before starting exercise program"])

def get_exercise_intensity(user_data):
    age = int(user_data['age'])
    bmi = float(user_data['bmi'])
    medical_condition = user_data['medicalCondition']
    
    high_risk_conditions = ['Coronary Heart Disease', 'Atrial Fibrillation', 'COPD', 
                           'Type 1 Diabetes', 'Multiple Sclerosis']
    
    if medical_condition in high_risk_conditions or bmi > 30 or age > 60:
        return "low"
    elif medical_condition == 'none' and bmi < 25 and age < 30:
        return "high"
    else:
        return "moderate"
def format_equipment_list(equipment):
    if not equipment:
        return "No equipment available"
    
    # Clean up equipment names for display
    equipment_names = [item.replace('equipment', '').title() for item in equipment]
    return ", ".join(equipment_names)

def create_workout_prompt(user_data):
    intensity = get_exercise_intensity(user_data)
    safety_guidelines = validate_medical_safety(user_data['medicalCondition'])
    available_equipment = format_equipment_list(user_data.get('equipment', []))
    
    prompt = f"""
    As a fitness expert called Vitality, create a personalized workout plan for a user with the following profile:
    
    USER PROFILE:
    - Age: {user_data['age']}
    - BMI: {user_data['bmi']}
    - Medical Condition: {user_data['medicalCondition']}
    - Current Body Type: {user_data['currentBodyType']}
    - Desired Body Type: {user_data['desiredBodyType']}
    - Recommended Intensity: {intensity}
    - Available Equipment: {available_equipment}
    
    Safety Considerations:
    {', '.join(safety_guidelines)}
    
    
    - DO NOT give anything other than what has been asked for!
    - DO NOT give overall progression
    - DO NOT give any diet or nutritional information
    - DO NOT give any information on how to do the exercise or form.

    Please provide:
    1. A detailed weekly workout plan including:
       - 5-7 specific exercises appropriate for their condition and available equipment
       - Sets and repetitions for each exercise
       - Rest periods and frequency
       - should be arranged in monday to sunday format
       - Include exercises that utilize their available equipment effectively
       - For any equipment-based exercises, specify which piece of equipment to use
   
    Format the response in a clear, structured way suitable for a text file.
    Focus on safety, especially considering their medical condition.
    """
    return prompt

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/saveExercises', methods=['POST'])
def save_exercises():
    try:
        user_data = request.json
        
        # Validate required fields
        required_fields = ['name', 'age', 'height', 'weight', 'bmi', 'medicalCondition', 
                         'currentBodyType', 'desiredBodyType']
        for field in required_fields:
            if field not in user_data:
                raise ValueError(f"Missing required field: {field}")
        
        # Generate workout plan using Gemini
        prompt = create_workout_prompt(user_data)
        response = model.generate_content(prompt)
        
        # Create the complete workout plan
        workout_plan = f"""
PERSONALIZED WORKOUT PLAN FOR {user_data['name'].upper()}

USER PROFILE:
- Age: {user_data['age']} years
- Height: {user_data['height']} cm
- Weight: {user_data['weight']} kg
- BMI: {user_data['bmi']}
- Medical Condition: {user_data['medicalCondition']}
- Current Body Type: {user_data['currentBodyType']}
- Desired Body Type: {user_data['desiredBodyType']}
- Available Equipment: {format_equipment_list(user_data.get('equipment', []))}

SAFETY GUIDELINES:
{chr(10).join('- ' + guideline for guideline in validate_medical_safety(user_data['medicalCondition']))}

WORKOUT RECOMMENDATIONS:
{response.text}

IMPORTANT NOTICE:
- Always consult with your healthcare provider before starting this exercise program
- Stop exercising immediately if you experience pain, dizziness, or severe discomfort
- Start slowly and gradually increase intensity as you build strength and endurance
- Stay properly hydrated and maintain good form throughout all exercises
- Monitor your condition and adjust the workout intensity as needed
- Only use equipment you are familiar with and confident in using safely
"""
        
        # Save to file
        filename = f"workout_plan_{user_data['name'].replace(' ', '_')}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(workout_plan)
        
        return jsonify({
            'success': True,
            'filename': filename,
            'message': 'Your personalized workout plan has been created successfully!'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)