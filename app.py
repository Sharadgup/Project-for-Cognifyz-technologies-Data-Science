import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model_path = 'restaurant_rating_prediction_model.joblib'  # Update this with the actual path to your model
model = joblib.load(model_path)

# Define a function to preprocess input data and predict restaurant rating
def predict_rating(restaurant_name):
    # Perform preprocessing on the input data
    input_data = preprocess_input(restaurant_name)
    
    if input_data is None:
        st.error("Error processing input data.")
        return None
    
    # Make predictions
    try:
        predicted_rating = model.predict(input_data)
        return predicted_rating[0]  # Assuming the model returns a single prediction
    except ValueError as e:
        st.error(f"Error occurred during prediction: {e}")
        return None

def preprocess_input(restaurant_name):
    # Example preprocessing steps (replace with your actual preprocessing steps)
    # Here, we are encoding the restaurant name and other features into numerical format
    # You may need to adjust this based on your actual data and preprocessing requirements
    encoded_data = pd.DataFrame({
        'Restaurant Name': [restaurant_name],
        # Add other features and encode them as needed
    })
    
    # Check if the encoded data has the expected format and return it
    if check_data_format(encoded_data):
        return encoded_data
    else:
        return None

def check_data_format(data):
    # Check if the data format is as expected by the model
    # For example, check if numerical columns are of correct data types
    # You may need to customize this based on your model's input requirements
    return True  # Placeholder, customize as needed

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
