"""
Write a function that raises a name exception with a message.

Prototype: def raise_exception_msg(message=""):
You are not allowed to import any module
"""

def raise_exception_msg(message=""):
    raise NameError(message)
try:
    raise_exception_msg("C is fun")
except NameError as ne:
    print(ne)