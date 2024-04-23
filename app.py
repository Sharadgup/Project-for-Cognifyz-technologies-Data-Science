import streamlit as st
import pandas as pd
import pickle
from google.colab import drive

# Mount Google Drive to access the model file
drive.mount('/content/drive')

# Load the trained model
model_path = '/content/restaurant_rating_prediction_model.pkl'  # Update this with the actual path to your model
try:
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    st.success("Model loaded successfully!")  # Print success message if model loads
except FileNotFoundError:
    st.error("Model file not found! Please check the file path.")
except Exception as e:
    st.error(f"Error loading the model: {e}")

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
