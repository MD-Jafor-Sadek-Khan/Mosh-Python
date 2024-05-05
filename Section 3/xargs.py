"""*args"""


def multiply(*args: int):
    """returs multiplied value of the passes arguments"""
    total: int = 1
    for arg in args:
        if not isinstance(arg, int):
            return "Not a number"
        total *= arg
    return total


print(multiply(1, 2, 3, 5))
