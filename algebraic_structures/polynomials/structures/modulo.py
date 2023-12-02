from fractions import Fraction

from algebraic_structures.polynomials.algorithms.egcd import egcd


class Modulo:
    """Число из кольца вычетов"""
    def to_modulo(self, value):
        if isinstance(value, Modulo):
            return value
        if isinstance(value, int):
            return Modulo(value, modulus=self.modulus)
        if isinstance(value, Fraction):
            assert value.denominator == 1
            return Modulo(value.numerator, modulus=self.modulus)

    def __init__(self, value: int, *, modulus: int):
        if isinstance(value, Modulo):
            value = value.value
        assert modulus > 0
        self.modulus = modulus
        self.value = value % modulus

    def __add__(self, other):
        other = self.to_modulo(other)
        if isinstance(other, Modulo):
            return Modulo(self.value + other.value, modulus=self.modulus)
        return NotImplemented

    def __radd__(self, other):
        other = self.to_modulo(other)
        return self.__class__.__add__(other, self)

    def __mul__(self, other):
        other = self.to_modulo(other)
        if isinstance(other, Modulo):
            return Modulo(self.value * other.value, modulus=self.modulus)
        return NotImplemented

    def __rmul__(self, other):
        other = self.to_modulo(other)
        if isinstance(other, Modulo):
            return Modulo(self.value * other.value, modulus=self.modulus)
        return NotImplemented

    def __truediv__(self, other):
        other = self.to_modulo(other)
        (gcd_, inv, _) = egcd(other.value, self.modulus)
        if gcd_ > 1:
            raise ValueError('congruence class has no inverse')

        return Modulo((self.value * inv) % self.modulus, modulus=self.modulus)

    def __neg__(self):
        return Modulo(-self.value, modulus=self.modulus)

    def __eq__(self, other):
        other = self.to_modulo(other)
        return self.value == other.value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

    def __bool__(self):
        return bool(self.value)


def mod5(value: int):
    return Modulo(value, modulus=5)
