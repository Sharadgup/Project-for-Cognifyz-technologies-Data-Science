import os
import streamlit as st
import pandas as pd
import pickle

# Check if 'scikit-learn' is installed
try:
    import sklearn
except ImportError:
    st.error("Error loading the model: 'scikit-learn' is not installed. Please install it using 'pip install scikit-learn'")
    st.stop()  # Stop execution if 'scikit-learn' is not installed

# Continue with loading the model
model_path = 'restaurant_rating_prediction_model.pkl'  # Update this with the actual path to your model

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
