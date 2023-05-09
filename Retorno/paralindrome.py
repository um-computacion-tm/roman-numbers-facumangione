import unittest
def paliendro(word):
    if len(word) <= 1:
        return True
    if word [0] == word[-1]:
        return paliendro (word[1:-1])
    else:
        return False

    
    
    
    
    


class TestPalindrome(unittest.TestCase):
    def test_palindro_simple(self):
        result = paliendro('neuquen')  
        self.assertEqual(result, True)

    def test_none_palindrome_simple(self):
        result = paliendro('pepe')    
        self.assertEqual(result, False)
        
if __name__ == '__main__':
    unittest.main()
