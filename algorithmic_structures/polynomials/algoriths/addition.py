from itertools import zip_longest
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from algorithmic_structures.polynomials.structures.polynomial import Polynomial


def add_polynomials(p1: 'Polynomial', p2: 'Polynomial') -> 'Polynomial':
    """Сложение двух полиномов"""
    result = []
    for c1, c2 in zip_longest(reversed(p1.coefficients), reversed(p2.coefficients)):
        result.append((c1 or 0) + (c2 or 0))
    result.reverse()
    return p1.__class__(result)
