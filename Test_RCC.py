import unittest
from Rotating_Caesar_Cipher import Rotating_CC

class Test_RCC(unittest.TestCase):
    
    def setUp(self):
        self.test_rcc = Rotating_CC()
        
    def test_encrypt_1(self):
        new_msg = self.test_rcc.RCC_encrypt("HELLO",0)
        self.assertEqual(new_msg, "HELLO")
    
    def test_encrypt_2(self):
        new_msg = self.test_rcc.RCC_encrypt("HELLO",2)
        self.assertEqual(new_msg, "JIRTY")
    
    def test_encrypt_3(self):
        new_msg = self.test_rcc.RCC_encrypt("Hello",2)
        self.assertEqual(new_msg, "Jirty")
        
    def test_encrypt_4(self):
        new_msg = self.test_rcc.RCC_encrypt("Hello",3)
        self.assertEqual(new_msg, "Kkuxd")
        
    def test_encrypt_5(self):
        new_msg = self.test_rcc.RCC_encrypt("Hello World!",3)
        self.assertEqual(new_msg, "Kkuxd Ojpmh!")
    
    def test_encrypt_6(self):
        new_msg = self.test_rcc.RCC_encrypt("Hello\n",2)
        self.assertEqual(new_msg, "Jirty\n")
        
    def test_encrypt_7(self):
        new_msg = self.test_rcc.RCC_encrypt(f"Hello{2+2}",2)
        self.assertEqual(new_msg, "Jirty4")
        
    def test_decrypt_1(self):
        new_msg = self.test_rcc.RCC_decrypt("HELLO",0)
        self.assertEqual(new_msg, "HELLO")
        
if __name__ == '__main__':
    unittest.main()
        