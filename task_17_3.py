def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


class Fraction:
    def __init__(self, number_1, number_2):
        self.top = number_1
        self.bottom = number_2

    def __add__(self, otherfraction):
        num = self.top * otherfraction.bottom + self.bottom * otherfraction.top
        den = self.bottom * otherfraction.bottom
        common = gcd(num, den)
        return Fraction(num // common, den // common)

    def __sub__(self, otherfraction):
        num = self.top * otherfraction.bottom - self.bottom * otherfraction.top
        den = self.bottom * otherfraction.bottom
        common = gcd(num, den)
        return Fraction(num // common, den // common)

    def __mul__(self, otherfraction):
        num = self.top * otherfraction.top
        den = self.bottom * otherfraction.bottom
        common = gcd(num, den)
        return Fraction(num // common, den // common)

    def __truediv__(self, otherfraction):
        num = self.top * otherfraction.bottom
        den = self.bottom * otherfraction.top
        common = gcd(num, den)
        return Fraction(num // common, den // common)

    def __floordiv__(self, otherfraction):
        num = self.top * otherfraction.bottom
        den = self.bottom * otherfraction.top
        common = gcd(num, den)
        return Fraction(num // common, den // common)

    def __gt__(self, otherfraction):
        num1 = self.top / self.bottom
        num2 = otherfraction.top / otherfraction.bottom
        if num1 > num2:
            return True
        else:
            return False

    def __lt__(self, otherfraction):
        num1 = self.top / self.bottom
        num2 = otherfraction.top / otherfraction.bottom
        if num1 < num2:
            return True
        else:
            return False

    #
    def __ge__(self, otherfraction):
        num1 = self.top / self.bottom
        num2 = otherfraction.top / otherfraction.bottom
        if num1 >= num2:
            return True
        else:
            return False

    def __le__(self, otherfraction):
        num1 = self.top / self.bottom
        num2 = otherfraction.top / otherfraction.bottom
        if num1 <= num2:
            return True
        else:
            return False

    def __str__(self):
        return f"Now the number is {self.top}/{self.bottom}"


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    # print(x + y == Fraction(3, 4))  # x <= y
    print(x <= y)
