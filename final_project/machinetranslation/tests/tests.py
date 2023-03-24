import unittest

from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_english_to_french_hello(self):
        result = english_to_french("Hello")
        self.assertEqual(result, "Bonjour")
        
    def test_french_to_english_bonjour(self):
            result = french_to_english("Bonjour")
            self.assertEqual(result, "Hello")
            
    def test_english_to_french_null_input(self):
        result = english_to_french(None)
        self.assertEqual(result, "Error: No input provided")
        
    def test_french_to_english_null_input(self):
        result = french_to_english(None)
        self.assertEqual(result, "Error: No input provided")

unittest.main()