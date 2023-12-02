from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from algorithmic_structures.polynomials.structures.polynomial import Polynomial


def multiply_by_number(p: 'Polynomial', k: float) -> 'Polynomial':
    result = [c * k for c in p.coefficients]
    return p.__class__(result)


def multiply_by_x_degree(p: 'Polynomial', degree: int) -> 'Polynomial':
    result = list(p.coefficients)
    result.extend([0] * degree)
    return p.__class__(result)


def multiply_polynomials(p1: 'Polynomial', p2: 'Polynomial'):
    from algorithmic_structures.polynomials.structures.polynomial import Polynomial
    result = Polynomial.ZERO
    for d1, c1 in enumerate(reversed(p1.coefficients)):
        for d2, c2 in enumerate(reversed(p2.coefficients)):
            result += multiply_by_x_degree(Polynomial.ONE, d1 + d2) * (c1 * c2)
    return result
