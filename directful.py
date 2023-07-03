import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
import os

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

stop_words = stopwords.words("english")

def cleaning(text):
 
    #1. Tokenize and lower
    text_tokens = word_tokenize(text.lower()) 
    
    #2. Remove Puncs and numbers
    tokens_without_punc = [w for w in text_tokens if w.isalpha()]
    
    #3. Removing Stopwords
    tokens_without_sw = [t for t in tokens_without_punc if t not in stop_words]
    
    #4. lemma
    text_cleaned = [WordNetLemmatizer().lemmatize(t) for t in tokens_without_sw]
    
    #joining
    return " ".join(text_cleaned)



vectorizer = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open("directful_model_new.pkl", "rb"))

st.title("SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):

    # 1. preprocess
    cleaning_sms = cleaning(input_sms)
    # 2. vectorize
    vector_input = vectorizer.transform([cleaning_sms])
    # 3. predict
    result = model.predict(vector_input)[0]
    # 4. Display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")




























