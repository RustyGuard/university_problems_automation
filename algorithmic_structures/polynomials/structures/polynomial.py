import math
from fractions import Fraction
from typing import Iterable, Type, Self

from algorithmic_structures.polynomials.algoriths.addition import add_polynomials
from algorithmic_structures.polynomials.algoriths.division import divide_with_remainder
from algorithmic_structures.polynomials.algoriths.inverse import inverse_polynomial
from algorithmic_structures.polynomials.algoriths.multiply import multiply_by_number, multiply_polynomials
from algorithmic_structures.polynomials.algoriths.utils import strip_zeros
from algorithmic_structures.polynomials.structures.modulo import Modulo


class Polynomial[T]:
    ONE: 'Polynomial'
    ZERO: 'Polynomial'

    def __init__(self, coefficients: Iterable[float], number_type: Type[T] = Fraction):
        """number_type - функция для преобразования значений к необходимому типу"""
        self.coefficients: tuple[T] = tuple(strip_zeros(coefficients, number_type)) or (number_type(0),)
        self.number_type = number_type

    def __str__(self):
        if not self:
            return '0'
        result = []
        for i, coefficient in enumerate(self.coefficients):
            if coefficient == 0:
                continue

            degree = len(self.coefficients) - i - 1
            if degree == 0:
                x_with_power = ''
            elif degree == 1:
                x_with_power = 'x'
            else:
                x_with_power = f'x^{degree}'

            if degree:
                if coefficient == 1:
                    coefficient = ''
                # if coefficient == -1:
                #     coefficient = '-'

            result.append(f'{coefficient}{x_with_power}')
        return ' + '.join(result)

    def __repr__(self):
        return str(self)

    @property
    def degree(self):
        """Степень многочлена"""
        if self.coefficients == [0]:
            return -math.inf
        return len(self.coefficients) - 1

    def __add__(self, other):
        if not isinstance(other, Polynomial):
            return NotImplemented
        return add_polynomials(self, other)

    def __mul__(self, other):
        if isinstance(other, (float, Fraction, int, Modulo)):
            return multiply_by_number(self, other)
        if isinstance(other, Polynomial):
            return multiply_polynomials(self, other)
        return NotImplemented

    def __divmod__(self, other):
        return divide_with_remainder(self, other)

    def __floordiv__(self, other):
        return divide_with_remainder(self, other)[0]

    def __mod__(self, other):
        return divide_with_remainder(self, other)[1]

    def __neg__(self):
        return inverse_polynomial(self)

    def __bool__(self):
        return self.coefficients != Polynomial.ZERO.coefficients

    def normalize(self) -> Self:
        """Нормализованный многочлен - многочлен первый коэффициент которого равен 1"""
        if not self:
            return self
        major = self.coefficients[0]
        return self.__class__((c / major for c in self.coefficients), number_type=self.number_type)


Polynomial.ONE = Polynomial((1,))
Polynomial.ZERO = Polynomial((0,))
