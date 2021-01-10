#this is the flask app for project_file

from flask import Flask, request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)
pickle_model = open('model.pkl', 'rb')
classifier = pickle.load(pickle_model)
pickle_bow_model = open('vectorizer.pkl', 'rb')
vectorizer = pickle.load(pickle_bow_model)

@app.route('/')
def welcome():
    return "WELCOME ALL"


@app.route('/predict')
def predict():
    sentence = request.args.get('sentence')
    vector = vectorizer.transform([str(sentence)])
    pred = classifier.predict(vector)
    
    if pred[0]:
        prediction = "Positive"
    else:
        prediction = "Negative"

    return 'prediction:'+str(prediction)


if __name__ == '__main__':
    app.run()