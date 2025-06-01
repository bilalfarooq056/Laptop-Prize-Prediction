import numpy as np
import streamlit as st
import pickle

# Load your trained model (use the correct file path)
try:
    with open('laptop_price_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    st.success("Model loaded successfully!")
except FileNotFoundError:
    st.error("Model file not found. Please train and save your model first.")
    model = None  # Set model to None if loading fails

features = ['Brand', 'Processor Generation', 'Processor Type', 'Processor Speed', 'Installed RAM',
            'SSD', 'Graphic Brand', 'Graphic Memory', 'Screen Resolution', 'TouchScreen', 
            'Finger Print Reader', 'Backlit keyboard', 'LAN', 'Color', 'Weight']

# Streamlit UI
st.title('Laptop Price Prediction App')

# Input fields
brand = st.selectbox('Brand', options=['acer', 'asus', 'dell', 'hp', 'lenovo', 'msi', 'microsoft', 'samsung', 'surface'])
processor_generation = st.selectbox('Processor Generation', options=[3, 5, 7, 9, 11, 12, 13, 14])
processor_type = st.selectbox('Processor Type', options=['Intel', 'AMD', 'Snapdragon'])
processor_speed = st.number_input('Processor Speed (in GHz)', min_value=2.5, max_value=5.0, step=0.8)
installed_ram = st.selectbox('Installed RAM (in GB)', options=[2,4,6,8,12,14,16,32,64])
ssd = st.selectbox('SSD (in GB)', options=[128,256,512,1024,2048])
graphic_brand = st.selectbox('Graphic Brand', options=['NVIDIA', 'NVIDIA RTX', 'AMD Ryzen', 'Qualcomm'])
graphic_memory = st.selectbox('Graphic Memory (in GB)', options=['2050','4050','4060','4070','4080', '4090'])
screen_resolution = st.selectbox('Screen Resolution', options=['1366x768', '1920x1080', '2560x1440', '3840x2160'])
touchscreen = st.selectbox('Touchscreen?', options=['Yes', 'No'])
finger_print_reader = st.selectbox('Finger Print Reader?', options=['Yes', 'No'])
backlit_keyboard = st.selectbox('Backlit Keyboard?', options=['Yes', 'No'])
lan = st.selectbox('LAN?', options=['Yes', 'No'])
color = st.selectbox('Color', options=['Black', 'White', 'Silver'])
weight = st.number_input('Weight (in kg)', min_value=2.0, max_value=6.0, step=0.1)

# Define mappings
Brand_mapping = {
    'acer': 1,
    'asus': 2,
    'dell': 3,
    'hp': 4,
    'lenovo': 5,
    'msi': 6,
    'microsoft': 7,
    'samsung': 8,
    'surface': 9
}
processor_type_mapping = {
    'Intel': '0',
    'AMD': '1',
    'Snapdragon': '2'
}
color_mapping = {'Black': 1, 'White': 2, 'Silver': 0}
screen_resolution_mapping = {
    '1366x768': 0,
    '1920x1080': 1,
    '2560x1440': 2,
    '3840x2160': 3
}
graphic_brand_mapping = {
    'Intel': '0',
    'NVIDIA': '1',
    'NVIDIA RTX': '2',
    'AMD Ryzen': '3',
    'Qualcomm': '4'
}

# Convert user data
brand = Brand_mapping[brand]
processor_type = processor_type_mapping[processor_type]
graphic_brand = graphic_brand_mapping[graphic_brand]
touchscreen = 1 if touchscreen == 'Yes' else 0
finger_print_reader = 1 if finger_print_reader == 'Yes' else 0
backlit_keyboard = 1 if backlit_keyboard == 'Yes' else 0
lan = 1 if lan == 'Yes' else 0
color = color_mapping[color]  # Use the mapping for color
screen_resolution = screen_resolution_mapping[screen_resolution]  # Use the mapping for screen resolution

if st.button('Predict Price'):
    if model:
        input_data = np.array([[brand, processor_generation, processor_type, processor_speed,
                                 installed_ram, ssd, graphic_brand, graphic_memory,
                                 screen_resolution, touchscreen, finger_print_reader,
                                 backlit_keyboard, lan, color, weight]])
        
        # Make prediction
        y_pred = model.predict(input_data)  
        
        # Placeholder for output
        st.write(f'Predicted Price: Rs {y_pred[0]:.2f}')  # Formatting the price to two decimal places
    else:
        st.error("Model not loaded. Unable to make predictions.")
