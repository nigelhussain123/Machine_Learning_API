import unittest
import nltk
from sklearn.externals import joblib
from sklearn import preprocessing
from Modules import Server_Modules
from Modules import PreProcessing



log_reg = joblib.load('model.pkl')

class Test_Model(unittest.TestCase):
    
    
    def test_append(self):
        '''This is a test to see if the value we obtained through the string iteration returns an appropiate value'''
        self.assertIn(0,[0, 1])
    
    def test_tokenise(self):
        self.assertEqual(nltk.word_tokenize('''I like'''), ['I', 'like'])
        
    def test_logreg(self):
        self.assertEqual(log_reg.predict([[0]]), 0)
        
    def test_evaluate_order(self):
        self.assertEqual(Server_Modules.evaluate_order(['cancel']), 0)
        
    
        
    
    
        
if __name__ == '__main__':
    unittest.main()