"""
Create your own implementation of a built-in function range, named in_range(),
which takes three parameters: `start`, `end`, and optional step.
Tips: See the documentation for `range` function
"""

class Range:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            if self.step >= 1:
                result = f'{self.start}'
                self.start += self.step
                return result
            elif self.step < 0:
                raise StopIteration
            else:
                raise ValueError( 'range() arg 3 must not be zero')
        else:
            raise StopIteration


res = Range(11,22,0)
for i in res:
    print(i)


