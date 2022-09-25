from mathena.core.misc import lcm
use_gpu = False
if use_gpu:
    from numba import jit


class Fraction(object):
    def __init__(self, numerator: int, denominator: int) -> None:
        self.numerator = numerator
        self.denominator = denominator

    def is_proper(self):
        return self.numerator >= self.denominator
    def __str__(self):
        return f"""{self.numerator}\n{chr(8254)}\n{self.denominator}"""

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise Exception("other number must be a <mathena.fraction.Fraction> object")
        return self.add(other)

    def __mul__(self, other):
        return self.multiply(other)

    def __truediv__(self, other):
        return self.divide(other)

    def __sub__(self, other):
        return self.subtract(other)

    def add(self, second):
        if self.denominator != second.denominator:
            _lcm = lcm(self.denominator, second.denominator)
            _multiply = _lcm / self.denominator
            _numerator = self.numerator * _multiply
            _multiply = _lcm / self.denominator
            numerator = second.numerator * _multiply
            return Fraction(_numerator+numerator, _lcm)
        else:
            return Fraction(self.numerator+second.numerator, self.denominator)


    def to_no(self):
            return self.numerator / self.denominator

    def multiply(self, other):
        return Fraction(self.numerator*other.numerator, self.denominator*self.denominator)

    def divide(self, other):
        return Fraction(self.numerator*other.denominator, self.denominator*self.numerator)

    def subtract(self, second):
        if self.denominator != second.denominator:
            _lcm = lcm(self.denominator, second.denominator)
            _multiply = _lcm / self.denominator
            _numerator = self.numerator * _multiply
            _multiply = _lcm / self.denominator
            numerator = second.numerator * _multiply
            return Fraction(_numerator-numerator, _lcm)
        else:
            return Fraction(self.numerator-second.numerator, self.denominator)
