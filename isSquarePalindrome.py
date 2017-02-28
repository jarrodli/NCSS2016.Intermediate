import math


def is_square_palindrome(n):
    rev = str(n)[::-1]
    if int(n) == int(rev):
        if (math.sqrt(n)).is_integer():
            print(True)
        else:
            print(False)
    else:
        print(False)


"""def is_square(n):
    t = 0
    while t < n:
        t += 1
    if t * t != n:
        return True
    else:
        return False"""


is_square_palindrome(input("Number: "))



