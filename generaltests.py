import unittest

from general import *


class GeneralTest (unittest.TestCase):

    def test_rot13_basic(self):
        self.assertEqual(rot13("Hello"), "Uryyb")
        self.assertEqual(rot13("URYyb"), "HELlo")
        self.assertEqual(rot13("123!"), "123!")

    def test_is_prime(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(17))
        self.assertFalse(is_prime(-5))
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(100))
        self.assertTrue(is_prime(997))

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("Racecar"))
        self.assertTrue(is_palindrome(" "))
        self.assertTrue(is_palindrome("12321"))
        self.assertFalse(is_palindrome("hello"))
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))

    def test_caesar_cipher(self):
        self.assertEqual(caesar_cipher("abc", 3), "def")
        self.assertEqual(caesar_cipher("XYZ", 4), "BCD")
        self.assertEqual(caesar_cipher("Hello, World!", 5), "Mjqqt, Btwqi!")
        self.assertEqual(caesar_cipher("Secret 123!", 13), "Frperg 123!")

    def test_are_anagrams(self):
        self.assertTrue(are_anagrams("listen", "silent"))
        self.assertTrue(are_anagrams("Triangle", "Integral"))
        self.assertFalse(are_anagrams("apple", "pale"))
        self.assertTrue(are_anagrams("Astronomer", "Moon starer"))

    def test_check_password_strength(self):
        self.assertTrue(check_password_strength("SecureP@ss123"))
        self.assertFalse(check_password_strength("weakpass"))
        self.assertFalse(check_password_strength("NoDigitsHere!"))
        self.assertTrue(check_password_strength("short!A1"))
        self.assertTrue(check_password_strength("GoodPass!2023"))

    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), [])
        self.assertEqual(fibonacci(1), [0])
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(7), 5040)

    def test_matrix_addition(self):
        a = [[1, 2], [3, 4]]
        b = [[5, 6], [7, 8]]
        expected = [[6, 8], [10, 12]]
        self.assertEqual(matrix_addition(a, b), expected)

        c = [[1, 2, 3], [4, 5, 6]]
        d = [[10, 20, 30], [40, 50, 60]]
        expected2 = [[11, 22, 33], [44, 55, 66]]
        self.assertEqual(matrix_addition(c, d), expected2)

        mismatched = [[1, 2, 3], [4, 5, 6]]
        invalid_matrix = [[10, 20, 30]]
        with self.assertRaises(ValueError):
            matrix_addition(mismatched, invalid_matrix)

    def test_pascal_triangle(self):
        self.assertEqual(pascal_triangle(0), [])
        self.assertEqual(pascal_triangle(1), [[1]])
        self.assertEqual(pascal_triangle(2), [[1], [1, 1]])
        self.assertEqual(pascal_triangle(5), [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]
        ])

if __name__ == '__main__':
    unittest.main()