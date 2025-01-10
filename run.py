import streamlit as st
import json 
import requests 

st.title("Text Classifier")

user_input = st.text_input("Enter a sentence:")

inputs={"review":user_input}
if st.button("Get score"):
    res= requests.post(url='https://83b8-35-185-132-75.ngrok-free.app/sentiment',data=json.dumps(inputs))
    st.subheader(f"Response = {res.json()}")
    # print(res)