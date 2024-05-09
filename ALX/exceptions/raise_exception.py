"""
Write a function that raises a type exception.

Prototype: def raise_exception():
You are not allowed to import any module
"""

def raise_exception():
    raise TypeError()

try:
    raise_exception()
except TypeError as te:
    print("Exception raised")