"""exercise"""


def fizz_buzz(number: int):
    """Fizz Buzz"""
    if not number % 3 and not number % 5:
        return "fizz buzz"
    if not number % 5:
        return "buzz"
    if not number % 3:
        return "fizz"

    return number


print(fizz_buzz(5))
