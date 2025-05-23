from collections import deque
import re


def is_palindrome() -> bool:
    str = input("Enter your string: ")

    str_clean = re.findall(r"\w", str.lower())
    char_deque = deque()
    for char in str_clean:
        char_deque.append(char)

    while len(char_deque) > 1:
        if char_deque.pop() != char_deque.popleft():
            print("String is not palindrome")
            return False

    print("String is palindrome")
    return True


is_palindrome()
