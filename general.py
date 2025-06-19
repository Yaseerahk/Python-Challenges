def rot13(phrase: str) -> str:
    """
    Apply the ROT13 cipher to the given phrase.

    :param phrase: The input text to encode.
    :return: Encoded text using ROT13.
    """
    result = []
    for char in phrase:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base + 13) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)


def is_prime(number: int) -> bool:
    """
    Determine if a number is prime.

    :param number: The integer to check.
    :return: True if the number is prime, otherwise False.
    """
    if number < 2:
        return False
    for i in range(2,int(number **0.5)+1):
        if number % i ==0:
            return False
    return True


def is_palindrome(phrase: str) -> bool:
    """
    Check if the given phrase is a palindrome.

    :param phrase: The input text to analyze.
    :return: True if the phrase is a palindrome, otherwise False.
    """
    cleaned=''.join(char.lower()for char in phrase if char.isalnum())
    return cleaned == cleaned[::-1]


def caesar_cipher(phrase: str, shift: int) -> str:
    """
    Encrypt a phrase using the Caesar cipher with a given shift.

    :param phrase: The text to encode.
    :param shift: The shift value for the cipher.
    :return: Encoded text using the Caesar cipher.
    """
    result = []
    for char in phrase:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = chr((ord(char) - base + shift) % 26 + base)
            result.append(shifted)
        else:
            result.append(char)
    return ''.join(result)


def are_anagrams(phrase1: str, phrase2: str) -> bool:
    """
    Determine if two phrases are anagrams of each other.

    :param phrase1: The first input phrase.
    :param phrase2: The second input phrase.
    :return: True if the phrases are anagrams, otherwise False.
    """
    clean1 = sorted(c for c in phrase1.lower() if c.isalnum())
    clean2 = sorted(c for c in phrase2.lower() if c.isalnum())
    return clean1 == clean2


def check_password_strength(password: str) -> bool:
    """
    Evaluate the strength of a given password.

    :param password: The password to analyze.
    :return: True if the password meets strength criteria, otherwise False.
    """
    import string
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    return len(password) >= 8 and has_upper and has_lower and has_digit and has_special

    # return bool()


def fibonacci(number: int) -> list:
    """
    Generate a Fibonacci sequence of a given length.

    :param number: The number of terms in the sequence.
    :return: A list containing the Fibonacci sequence.
    """
    if number <= 0:
        return []
    sequence = [0]
    if number > 1:
        sequence.append(1)
    while len(sequence) < number:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


def factorial(number: int) -> int:
    """
    Compute the factorial of a given number.

    :param number: The integer for which the factorial is calculated.
    :return: The factorial of the input number.
    """
    if number < 0:
        raise ValueError("Factorial is undefined for negative numbers.")
    result = 1
    for i in range(2, number + 1):
        result *= i
    return result


def matrix_addition(list_a: list, list_b: list) -> list:
    """
    Perform element-wise addition of two matrices.

    :param list_a: The first matrix as a list of lists.
    :param list_b: The second matrix as a list of lists.
    :return: The resulting matrix after addition.
    """
    if len(list_a) != len(list_b) or any(len(row_a) != len(row_b) for row_a, row_b in zip(list_a, list_b)):
        raise ValueError("Matrices must be the same size.")
    return [[a + b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(list_a, list_b)]
    # return list()


def pascal_triangle(n: int) -> list:
    """
    Generate the first n rows of Pascal's triangle.

    :param n: The number of rows to generate.
    :return: A list of lists representing Pascal's triangle.
    """
    triangle = []
    for row_num in range(n):
        row = [1]
        for col in range(1, row_num):
            row.append(triangle[row_num - 1][col - 1] + triangle[row_num - 1][col])
        if row_num > 0:
            row.append(1)
        triangle.append(row)
    return triangle
    # return list()