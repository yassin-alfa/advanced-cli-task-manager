import unittest

def add(a, b):
    return a + b

class TestMathOperations(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(2, 3), 5)  # ✅ Passes
        self.assertEqual(add(-1, 1), 0)  # ✅ Passes

if __name__ == "__main__":
    unittest.main()