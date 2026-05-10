# 🎓 Student Result Prediction App

A beginner-friendly Machine Learning web application that predicts student results based on attendance, marks, and assignment submissions.

🔗 Live Demo: https://student-performance-app-en4c3tsykfz9ekptd9xvcf.streamlit.app/

## 🚀 Features

- Predicts Pass/Fail result
- Calculates performance score
- Generates student grade
- Attendance eligibility validation
- Interactive Streamlit interface

## 📊 Prediction Logic

✅ Attendance must be ≥ 75%  
✅ Marks must be ≥ 35  
✅ Assignments submitted must be ≥ 2  

Performance Score:
```python
marks + (assignments * 10)
```
Grades:
- A → 90+
- B → 75+
- C → 50+
- D → Below 50

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Streamlit

## 📷 Screenshots

### Home Interface
![image alt](https://github.com/asvarshini/student-performance-app/blob/main/predication-message.png?raw=true)
### Prediction Output
![image alt](https://github.com/asvarshini/student-performance-app/blob/main/home-interface.png?raw=true)

### Validation Messages
![image alt](https://github.com/asvarshini/student-performance-app/blob/main/validation.png?raw=true)

---

## ⚠️ Note

This project was developed as part of my Machine Learning and Data Analytics learning journey using a Decision Tree Classifier.

---

## 👩‍💻 Author

Vaishnavi Yad  
GitHub: https://github.com/asvarshini
