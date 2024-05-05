"""Function Types"""


def greet(name: str):
    """prints greeting"""
    print(f"HI {name}")


def get_greeting(name: str):
    """returns greeting"""
    return f"HI {name}"


message: str = get_greeting("Rahat")
greet("Rahat")
print(message)
