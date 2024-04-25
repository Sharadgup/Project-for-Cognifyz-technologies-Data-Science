import streamlit as st
import pandas as pd
import joblib

# Load the pre-trained model
model_path = 'restaurant_rating_system.joblib'  # Update with the actual path to your model file
model = joblib.load(model_path)

# Streamlit app
st.title('Restaurant Rating Prediction')

# Input fields for features
rating_color = st.selectbox('Select rating color:', ['Green', 'Red'])
has_table_booking = st.selectbox('Has table booking?', ['Yes', 'No'])
has_online_delivery = st.selectbox('Has online delivery?', ['Yes', 'No'])
locality = st.text_input('Enter locality:')
city = st.text_input('Enter city:')

# Make prediction on user input
if st.button('Predict Rating'):
    input_data = [[rating_color, 1 if has_table_booking == 'Yes' else 0,
                   1 if has_online_delivery == 'Yes' else 0, locality, city]]
    input_df = pd.DataFrame(input_data, columns=['Rating color', 'Has Table booking',
                                                 'Has Online delivery', 'Locality', 'City'])
    predicted_rating = model.predict(input_df)
    st.success(f'Predicted rating: {predicted_rating[0]:.2f}')
