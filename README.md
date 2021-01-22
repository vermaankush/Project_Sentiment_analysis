# Project_Sentiment_analysis
This is the final year project of my graduation in B Tech IT from University Institute of Technology, Himachal Pradesh University, Shimla, Himachal Pradesh.
This is an ML app on stock sentiment analysis using the news headlines.
Dataset is in the form of top 25 news headlines related to the company and the index of the dataset is the date on which these headlines have been published.
We combine all the top 25 headlines into one single string (do some preprocessing) and apply various models and Random Forest works out to be the best classifier here.
After predicting we save the vectorizer and model in two pickle files. 
This app has been deployed using following strategies: 
a) Flask and Flasgger,
b) Streamlit and Heroku.
This repository contains all the files required for smooth functioning of this app.
The model.pkl file was around 29 MB and it exceeded the file size limit in github, so I uploaded it using the clone repository method.
