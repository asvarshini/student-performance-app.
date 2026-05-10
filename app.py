import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load dataset
df = pd.read_csv("data/students.csv")

# -----------------------------
# RESULT LOGIC
# -----------------------------
df['result'] = df.apply(
    lambda row: "Pass"
    if row['attendance'] >= 75
    and row['marks'] >= 35
    and row['assignments'] >= 2
    else "Fail",
    axis=1
)

# -----------------------------
# PERFORMANCE SCORE
# -----------------------------
df['performance'] = df['marks'] + (df['assignments'] * 10)

# -----------------------------
# GRADE LOGIC
# -----------------------------
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "D"

df['grade'] = df['performance'].apply(get_grade)

# -----------------------------
# TRAIN MODEL
# -----------------------------
X = df[['attendance', 'marks', 'assignments']]
y = df['result']

model = DecisionTreeClassifier()
model.fit(X, y)

# -----------------------------
# STREAMLIT UI
# -----------------------------
st.title("🎓 Student Result Prediction App")

st.write(
    "Enter attendance, marks, and assignment details to predict student result and performance."
)

# Empty input boxes
attendance = st.number_input(
    "Attendance (%)",
    min_value=0,
    max_value=100,
    value=None,
    placeholder="Enter attendance percentage"
)

marks = st.number_input(
    "Marks",
    min_value=0,
    max_value=100,
    value=None,
    placeholder="Enter marks"
)

assignments = st.number_input(
    "Assignments Submitted",
    min_value=0,
    max_value=6,
    value=None,
    placeholder="Enter assignments submitted"
)

# -----------------------------
# PREDICTION BUTTON
# -----------------------------
if st.button("Predict Result"):

    # Check empty inputs
    if attendance == "" or marks == "" or assignments == "":
        st.warning("⚠️ Please fill all fields.")
    
    else:
        # Convert inputs to integers
        attendance = int(attendance)
        marks = int(marks)
        assignments = int(assignments)

        # Predict result using ML model
        pred = model.predict([[attendance, marks, assignments]])[0]

        # Performance calculation
        performance = marks + (assignments * 10)

        # Grade calculation
        if performance >= 90:
            grade = "A"
        elif performance >= 75:
            grade = "B"
        elif performance >= 50:
            grade = "C"
        else:
            grade = "D"

        # Eligibility logic
        if attendance < 75:
            st.error("❌ Attendance is below 75%. Student is not eligible.")

        elif marks < 35:
            st.error("❌ Marks are below passing criteria.")

        elif assignments < 2:
            st.error("❌ Minimum assignment submissions not completed.")

        else:
            st.success(f"📌 Prediction: {pred}")
            st.write(f"⭐ Performance Score: {performance}")
            st.write(f"🏅 Predicted Grade: {grade}")

st.info("This prediction system is trained on student academic performance data.")
