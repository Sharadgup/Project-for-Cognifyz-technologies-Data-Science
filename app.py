import streamlit as st
import pandas as pd
import pickle

# Load the trained model
model_path = 'restaurant_rating_prediction_model.pkl'  # Update this with the actual path to your model
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Define a function to predict restaurant rating
def predict_rating(restaurant_name):
    # Perform any necessary preprocessing on the input data
    # For example, if your model expects a DataFrame with specific columns, prepare the data accordingly
    # Then, use the trained model to make predictions
    input_data = pd.DataFrame({'Restaurant Name': [restaurant_name]})
    predicted_rating = model.predict(input_data)
    return predicted_rating[0]  # Assuming the model returns a single prediction

# Streamlit app
st.title('Restaurant Rating Prediction')

# Input field for restaurant name
restaurant_name = st.text_input('Enter the name of the restaurant:')

# Predict button
if st.button('Predict Rating'):
    if restaurant_name:
        predicted_rating = predict_rating(restaurant_name)
        st.success(f'Predicted rating for {restaurant_name}: {predicted_rating:.2f}')
    else:
        st.warning('Please enter a restaurant name.')
