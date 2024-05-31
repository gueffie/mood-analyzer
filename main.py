import streamlit as st
import plotly.express as px
import os
import nltk
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer


st.title("Diary tone")
filepaths = os.listdir("diary")

books = []
for filepath in filepaths:
    with open(f"diary/{filepath}", "r") as file:
        books.append(file.read())




analyzer = SentimentIntensityAnalyzer()
print(type(analyzer))
scores = [analyzer.polarity_scores(book) for book in books]
print(scores)

positivity = []
for score in scores:
    positivity.append(score['pos'])

negativity = []

for score in scores:
    negativity.append(score['neg'])

st.subheader("Positivity")

figure_positive = px.line(x=filepaths, y=positivity,labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(figure_positive)

st.subheader("Negativity")

figure_negative = px.line(x=filepaths, y=negativity, labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(figure_negative)
