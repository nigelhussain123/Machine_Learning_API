### This is a list of modules that we used for the model python file###
import pandas as pd
from sklearn.model_selection import train_test_split



def extract_data():
    '''This function reads the csv file and returns the messages and case types'''
       
    tech_df = pd.read_csv('tech_test_data.csv')
    tech_customer_df = tech_df[tech_df.message_source == 'customer']
    tech_customer_modified_df = tech_customer_df[(tech_customer_df.message_number == 1)]
    messages, case_types = tech_customer_modified_df.message, tech_customer_modified_df.case_type

    return(messages, case_types)


def create_data(X, Y):
    '''This function returns the training and testing data to create the model'''
    
    train_X, test_X, train_Y, test_Y = train_test_split(X, Y,
                                                   train_size = .7,
                                                   test_size =  .3,
                                                   random_state = 123)
    
    train_X_df = pd.DataFrame(train_X)
    train_Y_df = pd.DataFrame(train_Y)
    test_X_df = pd.DataFrame(test_X)
    test_Y_df = pd.DataFrame(test_Y)
    
    return(train_X_df, train_Y_df, test_X_df, test_Y_df)