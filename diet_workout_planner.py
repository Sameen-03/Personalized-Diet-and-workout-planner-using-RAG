import streamlit as st
import google.generativeai as genai

# Configure Gemini API
def get_gemini_response(user_input):
    genai.configure(api_key="")  # Replace with your API Key
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    response = model.generate_content(user_input)
    return response.text

# Streamlit UI
st.title("Diet & Workout Planner using RAG")

# Personal Data
st.header("Personal Data")
name = st.text_input("Name")
age = st.number_input("Age", min_value=1)
weight = st.number_input("Weight (kg)", min_value=1.0)
height = st.number_input("Height (cm)", min_value=1.0)
gender = st.radio("Gender", ["Male", "Female", "Other"])
activity_level = st.selectbox("Activity Level", ["Sedentary", "Lightly Active", "Moderately Active", "Very Active"])

# Goals
st.header("Goals")
goals = st.multiselect("Select Your Goals", ["Muscle Gain", "Fat Loss", "Stay Active"])

# Nutrition Goals
st.header("Nutrition Goals")
total_calories = st.number_input("Calories", min_value=0)
protein = st.number_input("Protein (g)", min_value=0)
fat = st.number_input("Fat (g)", min_value=0)
carbs = st.number_input("Carbs (g)", min_value=0)
nutrition_goals = {
    'total_calories': total_calories,
    'protein': protein,
    'fat': fat,
    'carbs': carbs
}

# Notes Section
st.header("Your Notes")
note = st.text_area("Add a new note")
notes = []
if st.button("Add Note"):
    st.write(note)
    notes.append(note)

# AI-Powered Workout & Diet Plan
st.header("AI-Powered Diet & Workout Plan")
user_query = st.text_area("Ask AI for a personalized plan")
if st.button("Get Plan"):
    plan_prompt = (
        f"Generate a structured and personalized diet and workout plan based on the user's input. "
        f"User Profile: {age}-year-old {gender}, {weight}kg, {height}cm. "
        f"Activity Level: {activity_level}. "
        f"Fitness Goals: {', '.join(goals)}. "
        f"Nutrition Goals: {nutrition_goals}. "
        f"User Query: {user_query}. "
        f"Take into account the notes from the user: {notes}."
        f"Consider their activity level, fitness goals, and nutritional targets to create a comprehensive plan. "
        f"The response should include a detailed diet breakdown, suggested meals, workout recommendations, and tips. "
        f"Ensure the advice is actionable and easy to follow."
    )
    plan_response = get_gemini_response(plan_prompt)
    st.write(plan_response)
