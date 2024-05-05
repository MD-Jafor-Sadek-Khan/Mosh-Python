"""Scope"""

message: str = "A"


def function():
    """example function. does nothing"""
    message = "B"


print(message)
