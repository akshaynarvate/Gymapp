import numpy as np
import pandas as pd
import streamlit as st
import sklearn
import pickle
import warnings

warnings.filterwarnings("ignore")
model = pickle.load(open("Model.pkl","rb")) #loading the created model


st.set_page_config(page_title="GYM Application") #tab title

#prediction function
def predict_status(age, height, weight):
    input_data = np.asarray([age, height, weight])
    input_data = input_data.reshape(1,-1)
    prediction = model.predict(input_data)
    return prediction[0]

def main():

    # titling your page
    st.title("Fitness Prediction App")

    #getting the input
    age = st.text_input("Enter your Age")
    height = st.text_input("Enter your Height in feet")
    weight = st.text_input("Enter your Weight in kgs")

    #predict value
    diagnosis = ""

    if st.button("Predict"):
    
        diagnosis = predict_status(age, height, weight)
        if diagnosis=="Underweight":
            st.info("You're Under Weight")

        elif diagnosis=="Healthy":
            st.success("You're Healthy")

        elif diagnosis=="Overweight":
            st.warning("You're Over Weight")

        elif diagnosis=="Obese":
            st.error("Obesity!")

        else:
            st.error("Extremely Obese")
        
        st.write("Project by Akshay Narvate")
    
            
if __name__=="__main__":
    main()
