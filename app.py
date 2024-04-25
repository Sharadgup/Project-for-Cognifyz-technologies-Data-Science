import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer

# Load your CSV file from your local machine
file_path = 'https://drive.google.com/u/0/uc?id=1eS-q31uXdtdpSOg15g7SZ65rZjBM7gBO&export=download'
df = pd.read_csv(file_path)

# Preprocess the data (encode categorical features and handle missing values)
encoder = OneHotEncoder(drop='first')
imputer = SimpleImputer(strategy='mean')

# Check if 'Name Length' is in the DataFrame columns
if 'Name Length' in df.columns:
    df = df.drop(columns=['Name Length'])  # Remove 'Name Length' column if present

# Separate numerical and categorical columns
numerical_cols = df.select_dtypes(include=['number']).columns
categorical_cols = df.select_dtypes(include=['object']).columns

# Encode categorical columns
df_encoded = pd.DataFrame(encoder.fit_transform(df[categorical_cols]).toarray(),
                          columns=encoder.get_feature_names_out(categorical_cols))

# Merge encoded categorical columns with numerical columns
df_final = pd.concat([df_encoded, df[numerical_cols]], axis=1)

# Impute missing values
df_imputed = pd.DataFrame(imputer.fit_transform(df_final),
                           columns=df_final.columns)

# Train the DecisionTreeRegressor model
X = df_imputed.drop(columns=['Aggregate rating'])  # Features
y = df_imputed['Aggregate rating']  # Target variable
model = DecisionTreeRegressor(random_state=42)
model.fit(X, y)

# Streamlit app
st.title('Restaurant Rating Prediction')

# Input fields for features
rating_color = st.selectbox('Select rating color:', df['Rating color'].unique())
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
    input_encoded = encoder.transform(input_df)  # Encode input data
    input_imputed = imputer.transform(input_encoded)  # Impute missing values in input
    predicted_rating = model.predict(input_imputed)
    st.success(f'Predicted rating: {predicted_rating[0]:.2f}')
