# Python_Machine_Learning_API
A Machine Learning Restful API that predicts customer orders and extracts important metadata such as account number and order id


## Overview Python_ML_API_FE

I will start by first providing a brief overview of all of the folders and files in this first directory. The first file that we have to take account of is the tech_test_data.csv file. This csv is what we used to train our logistic regression model. Afterwards, I used 2 jupyter notebook files (Prototyping_Machine_Learning.ipynb, Prototyping_Account_Order.ipynb) to prototype the two steps in the machine learning process (the machine learning model and the order id/account number extraction). Afterwards, I then took what I did in the Prototyping Machine Learning and transformed that into a model.py, which was then used to create the model.pkl file that is used in the RESTful API. I then created the server.py file to handle the RESTful API. In addition, there are two unit test files (server_test.py and PreProcessing_test.py). There are also two python modules (NLP and Server_Modules) which handle the text preprocessing and server functions in the server process. The file called templates has the html file that was used to create a simple front end. The htmlconv folder has all of the results from the convergence tests. The final text file (Production.txt) describes how I would push this service into production. 


## How to run
To run this web service, first run the python file model.py (or the jupyter notebook) to load the model and then run server.py to run the web service. The server will be defined in the terminal and to use it, just enter something into the form and you click on the respective button. This will produce the wanted output. 



## Overview Python_Machine_Learning_API

The exact same files are here, with the exception of the html files, as we are entering things directly into the terminal. 

## How to run
Same as above, except enter in terminal

## Assumptions:

We will have to assume that they will enter the command (cancel or order status) in one line and that they will enter all of the required information in the same line as well (order id and account number in the same line)
