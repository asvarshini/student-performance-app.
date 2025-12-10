import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load dataset
df = pd.read_csv("data/students.csv")

# Create result column (Pass/Fail)
df['result'] = df.apply(
    lambda row: "Pass" if (row['attendance'] + row['marks'] + row['assignments'] * 10) >= 120 else "Fail",
    axis=1
)

# Create performance column
df['performance'] = df['attendance'] + df['marks'] + df['assignments'] * 10

# Create grade column
def get_grade(score):
    if score >= 180:
        return "A"
    elif score >= 150:
        return "B"
        return "C"
    else:
        return "D"

df['grade'] = df['performance'].apply(get_grade)

# Train model
X = df[['attendance', 'marks', 'assignments']]
y = df['result']

model = DecisionTreeClassifier()
model.fit(X, y)

# Streamlit UI
st.title("🎓 Student Result Prediction App")

st.write("Enter the student details to predict PASS or FAIL")

attendance = st.number_input("Attendance (%)", min_value=0, max_value=100)
marks = st.number_input("Marks", min_value=0, max_value=100)
assignments = st.number_input("Assignments Submitted", min_value=0, max_value=10)

if st.button("Predict Result"):
    pred = model.predict([[attendance, marks, assignments]])[0]

    performance = attendance + marks + (assignments * 10)

    if performance >= 180:
        grade = "A"
    elif performance >= 150:
        grade = "B"
    elif performance >= 120:
        grade = "C"
    else:
        grade = "D"

    st.success(f"📌 **Prediction:** {pred}")
    st.write(f"⭐ **Performance Score:** {performance}")
    st.write(f"🏅 **Predicted Grade:** {grade}")

# Show dataset
st.subheader("📄 Student Dataset")
st.dataframe(df)
