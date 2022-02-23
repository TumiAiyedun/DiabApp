
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from PIL import Image

st.write("""
# DIABETES STATUS PREDICTION APP
""")

image = Image.open('Diabetes IMAGE.jpg')
st.image(image)

model=pickle.load(open('class_model.pkl', 'rb'))
scaler=pickle.load(open('scaler2.pkl', 'rb'))

st.sidebar.header('User Input Parameters')

def user_input_features():
    GenHlth= st.selectbox('Health Rating',('Excellent','Good','Stable','Bad','Critical'))
    if GenHlth=='Excellent':
        GenHlth=5
    if GenHlth=='Good':
        GenHlth=4
    if GenHlth=='Stable':
        GenHlth=3
    if GenHlth=='Bad':
        GenHlth=2
    else:
        GenHlth=1
    CholCheck = st.selectbox('Cholesterol Level',('High','Low'))
    if CholCheck=='High':
        CholCheck=1
    else:
        CholCheck=0
        
    HighBp = st.selectbox('Blood Pressure Level', ('High','Low'))
    if HighBp=='High':
         HighBp=1
    else:
         HighBp=0
            
    AnyHealthcare = st.selectbox('Do you have a Health Care Plan',('Yes','No'))
    if AnyHealthcare=='Yes':
        AnyHealthcare=1
    else:
        AnyHealthcare=0
    
    PhysActivity= st.selectbox('Do you engage in regular Physical Activity',('Yes','No'))
    if PhysActivity =='Yes':
        PhysActivity = 1
    else:
        PhysActivity = 0
        
    Veggie= st.selectbox('Do you Take Vegetables',('Yes','No'))
    if Veggie=='Yes':
        Veggies=1
    else:
        Veggies=0
    data = {'GenHlth':GenHlth,
           'CholCheck':CholCheck,
           'HighBp':HighBp,
           'AnyHealthCare':AnyHealthcare,
           'PhysActivity':PhysActivity,
           'Veggies':Veggies}
    
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()
input_df = scaler.transform(input_df)

if st.button('PREDICT'):
    y_out=model.predict(input_df)
    if y_out[0]==1:
        st.write(f' You have a high risk of Diabetes')
    else:
        st.write(f' You are not at risk of Diabetes')
