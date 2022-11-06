"""
Create your own implementation of a built-in function enumerate, named `with_
index`, which takes two parameters: `iterable` and `start`, default is 0.
Tips: see the documentation for the enumerate function
"""


class WithIndex:
    def __init__(self, iterable: list, start=0):
        self.iterable = iterable
        self.start = start
        self.first_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.first_index < len(self.iterable):
            result = f"{self.start} {self.iterable[self.first_index]}"
            self.start += 1
            self.first_index += 1
            return result
        else:
            raise StopIteration


a = ['a', 'b', 'c', 'd']
b = [1, 2, 3, 4]

capt = WithIndex(a, 28799)
for elem in capt:
    print(elem)
print('\n', '_' * 30, '\n')
capt2 = WithIndex(b, 50)
for elem in capt2:
    print(elem)
