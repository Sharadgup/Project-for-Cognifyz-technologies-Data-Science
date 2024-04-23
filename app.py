import os
import streamlit as st
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor  # Import the appropriate model class from sklearn

# Update the model path to point to the local path where your model is stored
model_path = 'restaurant_rating_prediction_model.pkl'

if os.path.exists(model_path):
    try:
        with open(model_path, 'rb') as file:
            model = pickle.load(file)
        st.success("Model loaded successfully!")  # Print success message if model loads
    except Exception as e:
        st.error(f"Error loading the model: {e}")
else:
    st.error("Model file not found! Please check the file path.")

# Define a function to predict restaurant rating
def predict_rating(restaurant_name):
    # Check if the model is loaded successfully
    if 'model' not in globals():
        st.error("Model is not loaded. Please check the model file path.")
        return None

    # Perform any necessary preprocessing on the input data
    input_data = pd.DataFrame({'Restaurant Name': [restaurant_name]})

    # Make predictions
    try:
        predicted_rating = model.predict(input_data)
        return predicted_rating[0]  # Assuming the model returns a single prediction
    except Exception as e:
        st.error(f"Error occurred during prediction: {e}")
        return None

# Streamlit app
st.title('Restaurant Rating Prediction')

# Input field for restaurant name
restaurant_name = st.text_input('Enter the name of the restaurant:')

# Predict button
if st.button('Predict Rating'):
    if restaurant_name:
        predicted_rating = predict_rating(restaurant_name)
        if predicted_rating is not None:
            st.success(f'Predicted rating for {restaurant_name}: {predicted_rating:.2f}')
    else:
        st.warning('Please enter a restaurant name.')
