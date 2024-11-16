import os
import PIL
import google.generativeai as genai
import streamlit as st

# Set API key
os.environ['GEMINI_IMAGE_API_KEY'] = 'enter your api'
genai.configure(api_key=os.environ['GEMINI_IMAGE_API_KEY'])

# Function to generate a response from Gemini
def get_gemini_response(input_text, image):
    model = genai.GenerativeModel('GEMINI 1.5 PRO')
    # Generate response based on text and image
    if input_text != "":  # Check if there is any text input
        response = model.generate_content(input_text, image)
    else:
        response = model.generate_content(image)
    return response.text

# Streamlit app settings
st.set_page_config(page_title='Uncover Insights Hidden in Your Photos')
st.header('Uncover Insights Hidden in Your Photos')
st.markdown("<h3 style='font-size: 23px;'>Developed by : Syed Musharaf </h3>", unsafe_allow_html=True)

# User inputs for text and image
input_text = st.text_input('Enter your text', key='input')
upload_file = st.file_uploader('Upload your image for Analysis', type=['png', 'jpg', 'jpeg'])

# Initialize image variable
image = None
if upload_file is not None:
    image = PIL.Image.open(upload_file)  # Open the uploaded image
    st.image(image, caption='Your uploaded image', use_column_width=True)

# Submit button to trigger analysis
submit = st.button('Explain brief about the image')

# When the submit button is clicked
if submit:
    if image is not None:  # If image is uploaded
        response = get_gemini_response(input_text, image)
        st.header('The response is:')
        st.write(response)
    else:
        st.write('Please upload your image for analyzing and response process')
