from itertools import count

from algorithmic_structures.polynomials.structures.polynomial import Polynomial


def polynomial_gcd(p1: Polynomial, p2: Polynomial) -> 'Polynomial':
    """Наибольший общий делитель"""
    dividend = p1  # Делимое
    divider = p2  # Делитель

    for i in count(1):
        # print(dividend, divider)
        print(f'{i})')
        div, mod = divmod(dividend, divider)
        # print(f'{i}) ({dividend}) = ({divider}) * ({div}) + ({mod})')
        if not mod:
            break
        dividend = divider
        divider = mod
        print()

    return divider
