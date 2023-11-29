import streamlit as st
import numpy as np
import cv2
import tensorflow as tf
from PIL import Image
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input as mobilenet_v2_preprocess_input
import database

def app():

    
    st.title("Image Classification")
    st.sidebar.subheader("Input")

    models_list = ["MobileNetV2"]
    selected_model = st.sidebar.selectbox("Select the Model", models_list)

    MODELS = {
        "MobileNetV2": 'Model.h5',
    }

    uploaded_file = st.sidebar.file_uploader(
        "Choose an image to classify", type=["jpg", "jpeg", "png"]
    )

    
    if uploaded_file is None:
        img = Image.open('logo.jpg')
        img = img.resize((450,450))
        st.image(img)
    else:
        model = tf.keras.models.load_model('Model.h5')
        class_names = { 0:'Aloevera',
                1:'Amaranthus Viridis (Arive - Dantu)',
                2:'Amruthabali',
                3:'Arali',
                4:'Castor',
                5:'Mango',
                6:'Mint',
                7:'Neem',
                8:'Sandalwood',
                9:'Turmeric'
                }
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype = np.uint8)
        opencv_image = cv2.imdecode(file_bytes,1)
        opencv_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)
        resized = cv2.resize(opencv_image, (224,224))

        img = Image.open(uploaded_file)
        img = img.resize((224, 224))
        
    
        resized = mobilenet_v2_preprocess_input(resized)
        img_reshape = resized[np.newaxis,...]    
        predictions = model.predict(img_reshape)
        prediction = predictions.argmax()
        prob = predictions[0][prediction]
        
        confidence_score = prob*100
        confidence_score = round(confidence_score, 2)
        col1, col2 = st.columns(2)
        with col1:
            st.image(img, channels="RGB")
       
        with col2:
            st.header(class_names[prediction])
            st.text("According to model Prediction \n{}% this is the Image of {}".format(confidence_score,class_names[prediction]))
        database.data(class_names[prediction])   

        

    