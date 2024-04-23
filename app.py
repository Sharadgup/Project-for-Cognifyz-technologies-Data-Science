import streamlit as st
import pandas as pd
import pickle
import os  # Import the os module for file path operations

# Define the raw GitHub file path for your model
github_raw_url = 'https://raw.githubusercontent.com/Sharadgup/Project-for-Cognifyz-technologies-Data-Science/main'
model_filename = 'restaurant_rating_prediction_model.pkl'
model_path = os.path.join(github_raw_url, model_filename)

# Display the model path and check if the file exists
st.write(f"Model path: {model_path}")
file_exists = os.path.exists(model_filename)  # Use the filename directly for checking existence
st.write(f"File exists: {file_exists}")

if file_exists:
    try:
        with open(model_filename, 'rb') as file:
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
