#this is the project api using streamlit

from flask import Flask, request
import pandas as pd
import numpy as np
import pickle
import streamlit as st


pickle_model = open('model.pkl', 'rb')
classifier = pickle.load(pickle_model)
pickle_bow_model = open('vectorizer.pkl', 'rb')
vectorizer = pickle.load(pickle_bow_model)


def welcome():
    return "WELCOME ALL"


def predict(sentence):
       
    vector = vectorizer.transform([str(sentence)])
    pred = classifier.predict(vector)
    
    if pred[0]:
        prediction = "Positive"
    else:
        prediction = "Negative"

    return prediction


def main():
    st.title("Stock Sentiment Analyzer")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Stock Sentiment Analysis ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    sentence = st.text_input("Sentence","Type the concatenated News headlines Here")
    result=""
    if st.button("Predict"):
        result=predict(sentence)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("This is a stock sentiment analysis app. If you input few of the news headlines related to a comapny this app tells whether the stocks will go up or down in the next few days.")
        st.text("This App is built with Streamlit")
    

if __name__ == '__main__':
    main()