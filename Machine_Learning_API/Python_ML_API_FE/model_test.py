import unittest
from Modules import Model_Modules



class TestNLP(unittest.TestCase):
    
    def test_create_data(self):
        
        '''unit test the create data function'''
        
        self.assertEqual(len(Model_Modules.create_data([0,1,2,3,4],[0,1,2,3,4])), 4)
        
    def test_extract_data(self):
        
        '''unit test the extract_data function'''
        
        self.assertEqual(len(Model_Modules.extract_data()), 2)

        
if __name__ == '__main__':
    unittest.main()