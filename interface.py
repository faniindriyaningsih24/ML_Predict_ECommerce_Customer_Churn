import streamlit as st
import pickle
import pandas as pd


with open('final_model_rf.pkl', 'rb') as file:
    loaded_model = pickle.load(file)


with open('transformer_rf.pkl', 'rb') as file_preprocessor:
    transformer_load = pickle.load(file_preprocessor)

st.title('E-Commerce Customer Churn Prediction')

# User inputs for the features
Tenure = st.number_input('Tenure', min_value=0, step=1, value=0)
WarehouseToHome = st.number_input('Warehouse To Home', min_value=0, step=1, value=0)
NumberOfDeviceRegistered = st.number_input('Number Of Device Registered', min_value=0, step=1, value=0)
PreferedOrderCat = st.selectbox('Prefered Order Category', ['Laptop & Accessory', 'Mobile Phone', 'Fashion', 'Grocery', 'Others'])
SatisfactionScore = st.selectbox('Satisfaction Score', [1, 2, 3, 4, 5])
MaritalStatus = st.selectbox('Marital Status', ['Single', 'Married', 'Divorced'])
NumberOfAddress = st.number_input('Number Of Address', min_value=0, step=1, value=0)
Complain = st.selectbox('Complain', [1, 0])
DaySinceLastOrder = st.number_input('Day Since Last Order', min_value=0, step=1, value=0)
CashbackAmount = st.number_input('Cashback Amount', min_value=0, step=1, value=0)

# Create a DataFrame with the inputs
data = {
    'Tenure': [Tenure],
    'WarehouseToHome': [WarehouseToHome],
    'NumberOfDeviceRegistered': [NumberOfDeviceRegistered],
    'PreferedOrderCat': [PreferedOrderCat],
    'SatisfactionScore': [SatisfactionScore],
    'MaritalStatus': [MaritalStatus],
    'NumberOfAddress': [NumberOfAddress],
    'Complain': [Complain],
    'DaySinceLastOrder': [DaySinceLastOrder],
    'CashbackAmount': [CashbackAmount]
}

input_df = pd.DataFrame(data)

# Predict the target
if st.button('Predict Churn'):
    # Transform the input data using the loaded transformer
    input_transformed = transformer_load.transform(input_df)
    
    # Predict using the loaded model
    prediction = loaded_model.predict(input_transformed)
    
    if prediction[0] == 1:
        st.write('Customers churn')
    else:
        st.write('Customers no churn')

# Button to reset/flush
if st.button('Reset'):
    st.experimental_rerun()
