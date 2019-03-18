# Import libraries
import numpy as np
from flask import Flask, request, render_template
import subprocess
import pickle
from sklearn.externals import joblib
import pandas as pd
import numpy as np
import os as os
import re, string, unicodedata
import nltk
import contractions
import inflect
from bs4 import BeautifulSoup
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from Modules import PreProcessing
from Modules import Server_Modules


app = Flask(__name__)

@app.route('/api', methods=['GET', 'POST'])

def predict():
    
    '''This is the method that will allow us to determine the type of request'''
    
    # Load model and encoder
    model = joblib.load('model.pkl')
    enc = Server_Modules.return_labels()
    
    
    # get request from form
    print('Hello. How may I help you?')
    requests = input()
    
    assert isinstance(requests, str)
    
    # tokenise
    words = nltk.word_tokenize(requests)
        
    # return final order
    order = Server_Modules.evaluate_order(words)

            
    return('Message type {}'.format(enc.inverse_transform(order)))



  

@app.route('/account', methods=['GET', 'POST'])

def retrieve():
    '''This is the method that will allow us to retrieve the account number and order id'''
    
    # get request from form
    print('Hello. What is your account number and order ID?')
    requests = input()
    
    assert isinstance(requests, str)

    # tokenise everything
    requests_tokenised = nltk.word_tokenize(requests)
    
    # normalise tokens
    normalised_tokens = PreProcessing.normalize_request(requests_tokenised)
    
    # extract the account number
    AN = []
    for tokens in normalised_tokens:
        if tokens.isdigit():
            AN.append(tokens)
            
    # rejoin the normalised tokens
    joined = " ".join(normalised_tokens)
    
    # append order ID portion of string to list
    ID = []
    if 'order' in joined:
        ID.append(joined.split('order', 1)[1])
        
    # The ID number will always be in the first index.
    ID_token = nltk.word_tokenize(ID[0])
    return('Account Number: {} \n Order id: {}'.format(AN[0], ID_token[1]))


if __name__ == '__main__':
    app.debug = True
    app.run(port=5000, debug=True)