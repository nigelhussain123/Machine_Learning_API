### These are the modules that will be used in the server function ###

from sklearn.externals import joblib
from sklearn import preprocessing

model = joblib.load('model.pkl')


def return_labels():
    
    ''' This method will return the encoder and the labels as something that the logistic regression classifier
    can read'''
    
    enc = preprocessing.LabelEncoder()
    labels = ['cancel_order', 'order_status']
    enc.fit(labels)
    return(enc)


def evaluate_order(tokens):
    
    ''' This method will determine what type of order is coming through'''

    if 'cancel' in tokens:
        prediction = model.predict([[0]])
    elif 'cancelling' in tokens:
        prediction = model.predict([[0]])
    elif 'canceled' in tokens:
        prediction = model.predict([[0]])
    else:
        prediction = model.predict([[1]])
     
    return(prediction)