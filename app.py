import streamlit as st
import joblib
import pandas as pd

model = joblib.load("model.pkl")

st.title("Student Performance Predictor")

st.write("Predict whether a student is likely to pass or fail.")

studytime = st.number_input("Study Time", min_value=1, max_value=4, value=2)
failures = st.number_input("Past Failures", min_value=0, max_value=4, value=0)
absences = st.number_input("Absences", min_value=0, max_value=100, value=5)
Medu = st.number_input("Mother's Education Level", min_value=0, max_value=4, value=2)
Fedu = st.number_input("Father's Education Level", min_value=0, max_value=4, value=2)

if st.button("Predict"):
    input_data = pd.DataFrame({
        "studytime": [studytime],
        "failures": [failures],
        "absences": [absences],
        "Medu": [Medu],
        "Fedu": [Fedu]
    })

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("Prediction: PASS")
    else:
        st.error("Prediction: FAIL")
