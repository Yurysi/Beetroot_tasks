"""
    Task 1

    Write a Python program to detect the number of local variables declared
    in a function.
    """


def scope():
    a = 25.5
    b = 5
    str_ = 'Tutorialspoint'


# main
print("Number of local varibales available:",
      scope.__code__.co_nlocals)
