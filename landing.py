import streamlit as st

def run():
    st.title("Doctor AI")
    
    # Load your image
    image_path = "DoctorAI.png"
    
    
    st.write("Welcome to our Disease Prediction Platform.")
    st.write("Our model predicts the likelihood of a disease based on your symptoms.")
    # Display the image on the landing page
    st.image(image_path, use_column_width=True)