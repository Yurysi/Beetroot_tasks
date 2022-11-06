"""
Create your own implementation of an iterable, which could be used inside
for-in loop. Also, add logic for retrieving elements using square
brackets syntax.
"""


class Custom:
    def __init__(self, holding_car, cars: list):
        self._holding = holding_car
        self._cars = cars

    def func(self, any):
        return any + " is a German brand!"

    def __iter__(self):
        return (self.func(name) for name in self._cars)


cars = Custom("VW Auto Group", ["VW", "Bugatti", "AUDI", "Porsche"])

for i in cars:
    print(i)

print(list(cars))
