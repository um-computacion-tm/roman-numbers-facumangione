import unittest

def binario_to_decimal(n):
   if n > 1:
       binario_to_decimal(n//2)
    return(n%2, end="")
 
    
bin = binario_to_decimal(n=)    
              







class TestNumeracion(unittest.TestCase):
    def test_binario_to_decimal(self):
        self.assertEqual(binario_to_decimal('01011100'), 92)

    def test_binario_to_decimal(self):    
        self.assertEqual(binario_to_decimal(97),'01100001')
        
if __name__ == '__main__':
    unittest.main()


