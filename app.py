import streamlit as st
import pandas as pd
import pickle
import requests  # Import requests library for downloading the model file

# Define the URL of the model file on GitHub
model_url = 'https://github.com/Sharadgup/Project-for-Cognifyz-technologies-Data-Science/blob/main/restaurant_rating_prediction_model.pkl'

# Display the model URL
st.write(f"Model URL: {model_url}")

# Function to download the model file
def download_model(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        else:
            st.error(f"Failed to download the model file. Status code: {response.status_code}")
            return None
    except Exception as e:
        st.error(f"Error downloading the model file: {e}")
        return None

# Download the model file
model_content = download_model(model_url)

# Check if the model file was downloaded successfully
if model_content is not None:
    try:
        # Load the model from the downloaded content
        model = pickle.loads(model_content)
        st.success("Model loaded successfully!")  # Print success message if model loads
    except Exception as e:
        st.error(f"Error loading the model: {e}")
else:
    st.error("Model file not found or download failed! Please check the URL.")

# Define a function to predict restaurant rating
def predict_rating(restaurant_name):
    # Check if the model is loaded successfully
    if 'model' not in globals():
        st.error("Model is not loaded. Please check the model URL.")
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
