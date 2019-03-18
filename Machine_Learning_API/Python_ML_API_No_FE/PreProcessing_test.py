import unittest
from Modules import PreProcessing


class TestNLP(unittest.TestCase):
    
    def test_contractions(self):
        self.assertEqual(PreProcessing.replace_contractions('''I'd'''), 'I would')
        
    def test_lower_case(self):
        self.assertEqual(PreProcessing.to_lowercase('ASD'), ['a', 's', 'd'])
        
    def test_remove_punctuation(self):
        self.assertEqual(PreProcessing.remove_punctuation(['a',',','s']), ['a', 's'])
        
    def test_replace_numbers(self):
        self.assertEqual(PreProcessing.replace_numbers(['a','1','s']), ['a', 'one', 's'])
        
    def test_remove_stop_words(self):
        self.assertEqual(PreProcessing.remove_stopwords(['three','is','sit']), ['three', 'sit'])
        
    def test_normalise(self):
        self.assertEqual(PreProcessing.normalize(['three','is', ',', 'sit']), ['three', 'sit'])
        
    def test_normalise_request(self):
        self.assertEqual(PreProcessing.normalize_request(['three','is', ',', 'sit']), ['three', 'sit'])
        
    
    
        
if __name__ == '__main__':
    unittest.main()