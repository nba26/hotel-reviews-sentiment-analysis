import streamlit as st
import joblib

# Load the trained model and vectorizer
model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Streamlit App UI
st.title("Hotel Review Sentiment Analysis")

# User input
user_input = st.text_area("Enter a hotel review:")

if st.button("Analyze Sentiment"):
    if user_input:
        # Transform input text using the vectorizer
        input_vector = vectorizer.transform([user_input])
        
        # Make prediction
        prediction = model.predict(input_vector)
        
        # Display result
        sentiment = "Positive" if prediction[0] == 1 else "Negative"
        st.write(f"Sentiment: **{sentiment}**")
    else:
        st.warning("Please enter a review to analyze.")