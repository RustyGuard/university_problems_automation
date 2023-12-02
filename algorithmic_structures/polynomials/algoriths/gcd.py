from itertools import count

from algorithmic_structures.polynomials.config import Config
from algorithmic_structures.polynomials.structures.polynomial import Polynomial


def polynomial_gcd(p1: Polynomial, p2: Polynomial) -> 'Polynomial':
    """Наибольший общий делитель"""
    dividend = p1  # Делимое
    divider = p2  # Делитель

    for i in count(1):

        if Config.SHOW_INTERMEDIATE_CALCULATIONS:
            print(f'{i})')
        div, mod = divmod(dividend, divider)

        if not mod:
            break
        dividend = divider
        divider = mod
        if Config.SHOW_INTERMEDIATE_CALCULATIONS:
            print()

    return divider
