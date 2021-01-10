#this is the frontend to my project using flasgger

from flask import Flask, request
import pandas as pd
import numpy as np
import pickle
from flasgger import Swagger

app = Flask(__name__)

Swagger(app)

pickle_model = open('model.pkl', 'rb')
classifier = pickle.load(pickle_model)
pickle_bow_model = open('vectorizer.pkl', 'rb')
vectorizer = pickle.load(pickle_bow_model)

@app.route('/')
def welcome():
    return "WELCOME ALL"


@app.route('/predict', methods = ["Get"])
def predict():
    
    """Let's predict the fall or rise of stocks using the news headlines
    This is using docstrings for specifications.
    ---
    parameters:
        - name: sentence
          in: query
          type: string
          required: true
    responses:
      200:
          description: The output value
    """
    
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