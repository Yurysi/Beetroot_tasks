"""
    Write a Python program to access a function inside a function (Tips: use
    function, which returns another function)
"""


def operation():
    def add(a, b):
        c = a * b
        return c

    return add


func1 = operation()
print(func1(2, 4.5))
