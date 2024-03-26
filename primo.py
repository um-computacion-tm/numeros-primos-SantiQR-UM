import unittest


def is_primo(value):
    for i in range(1, value+1):
        if value % i == 0 and value != i and i != 1 and value != 1:
            return False
    if value == 0:
        return False
    else:
        return True

class TestPrimos(unittest.TestCase):
    def test_0(self):
       result = is_primo(0)
       self.assertEqual(result, False)
    
    def test_1(self):
       result = is_primo(1)
       self.assertEqual(result, True)

    def test_2(self):
       result = is_primo(2)
       self.assertEqual(result, True)

    def test_3(self):
       result = is_primo(3)
       self.assertEqual(result, True)

    def test_4(self):
       result = is_primo(4)
       self.assertEqual(result, False)

    def test_15(self):
       result = is_primo(15)
       self.assertEqual(result, False)

if __name__ == "__main__":
    unittest.main()