import unittest

from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase):
    def test_e2f(self):
        self.assertEqual(english_to_french(' '), ' ')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Goodbye'), 'Auf Wiedersehen')
    
class TestF2E(unittest.TestCase):
    def test_f2e(self):
        self.assertEqual(french_to_english(' '), ' ')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Bonsoir'), 'Gute Nacht')

if __name__ == '__main__':
    unittest.main()