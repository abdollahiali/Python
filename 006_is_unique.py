import unittest

def is_unique(str):
    if len(str) > 128:
        return False
    
    flag_char_exist = [False]*128
    
    for i in range(len(str)):
        val = ord(str[i])
        if flag_char_exist[val]:
            return False
        flag_char_exist[val] = True
    return True

class Test(unittest.TestCase):
    
    data = [('', True),
         ('a', True),
         ('aA', True),
         ('Tt', True),
         ('AbCd012', True),
         ('0', True), 
         ('\n\r', True),
         ('\n\t\t', False),
         ('&**', False),
         ('^&%$', True),
         ('This is not unique', False),
         ('This unqe', True),
         ('This no uniq', False)]
    
    def test_is_unique(self):
        for (str, result) in self.data:
            self.assertTrue(is_unique(str) == result)
            
if __name__ == "__main__":
    unittest.main()
    
    