from typing import TYPE_CHECKING

from algorithmic_structures.polynomials.config import Config
from algorithmic_structures.polynomials.algoriths.multiply import multiply_by_x_degree

if TYPE_CHECKING:
    from algorithmic_structures.polynomials.structures.polynomial import Polynomial


def divide_with_remainder(p1: 'Polynomial', p2: 'Polynomial'):
    """Использует алгоритм Евклида для деления двух многочленов"""
    from algorithmic_structures.polynomials.structures.polynomial import Polynomial
    result = Polynomial.ZERO
    current_remainder = p1

    lines_to_print = []

    while current_remainder and current_remainder.degree >= p2.degree:
        degree_difference = current_remainder.degree - p2.degree
        major_ratio = current_remainder.coefficients[0] / p2.coefficients[0]
        if Config.SHOW_INTERMEDIATE_CALCULATIONS:
            lines_to_print.append(str(current_remainder))
        result += (
            multiply_by_x_degree(
                Polynomial.ONE * major_ratio,
                degree_difference
            )
        )

        subtrahend = multiply_by_x_degree(  # Вычитаемое
            p2 * major_ratio,
            degree_difference
        )
        if Config.SHOW_INTERMEDIATE_CALCULATIONS:
            lines_to_print.append(str(subtrahend))
            lines_to_print.append('-' * len(lines_to_print[-1]))

        current_remainder += -subtrahend

    if Config.SHOW_INTERMEDIATE_CALCULATIONS:
        lines_to_print.append(str(current_remainder))
        max_width = len(max(lines_to_print, key=len))
        a, b, c = lines_to_print.pop(0), lines_to_print.pop(0), lines_to_print.pop(0)
        print(a.rjust(max_width, ' ') + ' | ' + str(p2))
        print(b.rjust(max_width, ' ') + ' |-' + '-' * len(str(p2)))
        print(c.rjust(max_width, ' ') + ' | ' + str(result))
        for line in lines_to_print:
            print(line.rjust(max_width))

    return result, current_remainder
