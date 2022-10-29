"""
Write a decorator `arg_rules` that validates arguments passed to the function.

A decorator should take 3 arguments:

max_length: 15

type_: str

contains: [] - list of symbols that an argument should contain

If some of the rules' checks returns False, the function should return False
and print the reason it failed; otherwise, return the result.
"""


def arg_rules(type_: type, max_length: int, contains: list):
    def inner(func):
        def wrapper(*args):
            if type(args[0]) is type_:
                if len(args[0]) <= max_length:
                    issues = 0
                    for contain in contains:
                        if contain in args[0]:
                            issues += 1
                    if issues == 0:
                        print(func(*args))
                        return func
                    else:
                        print(f"Name {args[0]} have invalid {issues} values")
                else:
                    print(f'{args[0]} is False length')
            else:
                print("You must write only string")

        return wrapper

    return inner


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


# create_slogan('johndoe05@gmail.com')
#
# create_slogan('S@SH05')  # == 'S@SH05 drinks pepsi in his brand new BMW!'
create_slogan(121)
