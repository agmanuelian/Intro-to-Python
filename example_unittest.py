import unittest

def multiply_two(value):
    return value*2

class test_my_class(unittest.TestCase):

    def testequal(self):
        self.assertEqual(4, multiply_two(2))
    
    def testtrue(self):
        self.assertTrue(True)

unittest.main()




