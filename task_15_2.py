"""
Doggy age

Create a class Dog with class attribute `age_factor` equals to 7.
Make __init__() which takes values for a dog’s age. Then create a method
`human_age` which returns the dog’s age in human equivalent.
"""


class Dog():
    age_factor = 0

    def human_equivalent(self, age_factor):
        self.age_factor = age_factor * 7
        print(f"Your dog have {self.age_factor} age in human equivalent.")


pet = Dog()
pet.human_equivalent(4)
