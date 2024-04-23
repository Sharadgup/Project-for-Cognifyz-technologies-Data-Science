import streamlit as st
import pandas as pd
import pickle
import folium
import os

# Check the current working directory for debugging
print("Current Working Directory:", os.getcwd())

# Define the model path
model_path = 'restaurant_rating_prediction_model.pkl'  # Update with absolute file path
print("Model Path:", model_path)  # Print the model path for debugging

# Check if the model file exists and load the model
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

# Load your dataset that contains latitude and longitude columns
df = pd.read_csv('your_dataset.csv')  # Update with your actual dataset file path

# Create a map centered on the first location in your dataset (adjust as needed)
first_location = df.iloc[0]  # Assuming the first row contains latitude and longitude
map_center = [first_location['Latitude'], first_location['Longitude']]

# Create the map centered on the first location
my_map = folium.Map(location=map_center, zoom_start=10)

# Add markers for each location in your dataset
for index, row in df.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']], popup=row['Restaurant Name']).add_to(my_map)

# Display the map
st.markdown(my_map._repr_html_(), unsafe_allow_html=True)

