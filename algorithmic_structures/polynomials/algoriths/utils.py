from numbers import Number
from typing import Iterable

from algorithmic_structures.polynomials.config import Config


def strip_zeros[T](coefficients: Iterable[T]) -> Iterable[T]:
    """Обрубить начальные нули"""
    coefficients = iter(coefficients)
    for value in coefficients:
        if value:
            yield value
            break
    for c in coefficients:
        yield c


def convert_to_config_type(coefficients: Iterable[Number]) -> Iterable[Config.NUMERIC_TYPE_FOR_COEFFICIENTS]:
    for coefficient in coefficients:
        yield Config.NUMERIC_TYPE_FOR_COEFFICIENTS(coefficient)
