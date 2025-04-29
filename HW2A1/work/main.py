import unittest
from task import mystery_func

class TestCase(unittest.TestCase):
    def test1(self):
        a = 1
        b = 3
        self.assertFalse(mystery_func(a,b),msg='Does not meet the requirements (a={}, b={})'.format(a,b))

    def test2(self):
        a = 5
        b = 9
        self.assertTrue(mystery_func(a,b),msg='Does not meet the requirements (a={}, b={})'.format(a,b))

if __name__ == '__main__':
    unittest.main(verbosity=2)