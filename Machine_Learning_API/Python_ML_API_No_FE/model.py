# Import dependencies
import pandas as pd
import numpy as np
import os as os
import re, string, unicodedata
import nltk
import contractions
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
from Modules import PreProcessing
from sklearn.externals import joblib
from Modules import Server_Modules
from Modules import Model_Modules

# Load the dataset in a dataframe object and include the features

##########Data Preprocessing/Feature Extraction###############

# Extract the data
messages, case_types = Model_Modules.extract_data()


# List all Messages
message_list = list(messages)


# remove all of the contractions
message_preprocessed_list = [PreProcessing.replace_contractions(message) for message in message_list]


# tokenise the data
message_tokenised_list = [nltk.word_tokenize(string) for string in message_preprocessed_list]


# normalise the data

message_normalised_list = [PreProcessing.normalize(tokens) for tokens in message_tokenised_list]
    

# encode the messages
message_encoding = []

for tokens in message_normalised_list:
    if 'cancel' in tokens:
        message_encoding.append(0)
    elif 'cancelling' in tokens:
        message_encoding.append(0)
    elif 'cancelled' in tokens:
        message_encoding.append(0)
    else:
        message_encoding.append(1)


# convert to array
encoding_final_array = np.asarray(message_encoding)


# # Create the labels and Pre-process the testing data
enc = Server_Modules.return_labels()
case_types_preprocessed = enc.transform(case_types)


# Create training and testing data


train_X_df, train_Y_df, test_X_df, test_Y_df = Model_Modules.create_data(encoding_final_array, case_types_preprocessed)


# Logistic Regression classifier
lr = LogisticRegression()
lr.fit(train_X_df, train_Y_df)
results = lr.predict(test_X_df)


# Save your model
joblib.dump(lr, 'model.pkl')
print("Model dumped!")