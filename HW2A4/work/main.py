import unittest
from task import mystery_func2
class TestCase(unittest.TestCase):
    def test1(self):
        a = 2
        self.assertGreater(mystery_func2(a),0)

    def test2(self):
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)