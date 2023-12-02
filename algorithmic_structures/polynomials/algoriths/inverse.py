from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from algorithmic_structures.polynomials.structures.polynomial import Polynomial


def inverse_polynomial(p: 'Polynomial') -> 'Polynomial':
    return p.__class__((-c for c in p.coefficients), number_type=p.number_type)
