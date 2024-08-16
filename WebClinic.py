import streamlit as st
from joblib import load
import numpy as np
import pandas as pd

# Load pre-trained models and data
doctor = load('Doctor.joblib')
label_encoder = load('Encoder.joblib')
X, _, _, _ = load('DataSet.joblib')

# Function to create input mask for the model
def check(*position_1):
    mask = list(np.zeros(len(X.columns)))
    for pos in position_1:
        mask[X.columns.get_loc(pos)] = 1
    inp = pd.DataFrame([mask], dtype=int, columns=X.columns)
    return inp

# Function to predict disease based on symptoms
def predict_disease(symptoms):
    inp_mask = check(*symptoms)
    report = doctor.predict(inp_mask)
    return label_encoder.inverse_transform(report)[0]

# Streamlit app
def run():
    st.title("General Disease Prediction App")

    st.write("""
    Our model predicts the disease based on the symptoms provided by the user.
    """)

    # Symptom selection
    choices = list(X.columns)
    choices.sort()
    symptoms = st.multiselect(
        'Select your symptoms',
        choices
    )

    if st.button('Predict'):
        if symptoms:
            disease = predict_disease(symptoms)
            st.success(f'Most likely you have: {disease}')
        else:
            st.error('Please select at least one symptom.')
