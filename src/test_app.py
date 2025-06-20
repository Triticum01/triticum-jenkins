import unittest
from app import greet

class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("World"), "Hello, World!")
        self.assertEqual(greet("Jenkins"), "Hello, Jenkins!")

    def test_greet_empty(self):
        self.assertEqual(greet(""), "Hello, !")

if __name__ == '__main__':
    unittest.main()
