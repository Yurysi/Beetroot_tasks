"""
Custom exception

Create your custom exception named `CustomException`, you can inherit from
base Exception class, but extend its functionality to log every error message
to a file named `logs.txt`. Tips: Use __init__ method to extend functionality
for saving messages to file
"""
class CustomException(Exception):

    def __init__(self, msg):
        if msg:
            self.msg = msg
            with open('logs.txt', 'w') as issue:
                issue.write(self.msg)

def this_error(name, age):
    if age < 18:
        raise CustomException(f"{name} is {age}. He can't drive car.")
    else:
        print(f"{name} has {age}. He drives car to work")
# print(c)
# this_error("Andrew", 13)
this_error("Yura", 25)
this_error("Zhenya", 15)