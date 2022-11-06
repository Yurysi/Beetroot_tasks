from functools import wraps
# Task 3 from lesson 18
print("Task 3 from lesson 18\n")


class TypeDecorators:

    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return int(func(*args, **kwargs))
            except Exception as error:
                return f"{error.__class__.__name__}: {error}"
        return wrapper


    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return str(func(*args, **kwargs))
            except Exception as error:
                return f"{error.__class__.__name__}: {error}"
        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return bool(func(*args, **kwargs))
            except Exception as error:
                return f"{error.__class__.__name__}: {error}"

        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return float(func(*args, **kwargs))
            except ValueError as error:
                return f"{error.__class__.__name__}: {error}"

        return wrapper


@TypeDecorators.to_int
def to_do_int(string: str):
   return string

@TypeDecorators.to_str
def to_do_str(string: str):
   return string

@TypeDecorators.to_bool
def to_do_bool(string: str):
   return string

@TypeDecorators.to_float
def to_do_float(string: str):
   return string

print(type(to_do_int('55')))
print(to_do_int('55'))

print(type(to_do_str(55)))
print(to_do_str(55))

print(type(to_do_bool('4')))
print(to_do_bool('4'))

print(type(to_do_float('sf')))
print(to_do_float('-5'))