from numbers import Number
from typing import Iterable, Type


def strip_zeros[T](coefficients: Iterable[Number], number_type: Type[T]) -> Iterable[T]:
    """Обрубить начальные нули"""
    if not number_type:
        number_type = lambda x: x
    coefficients = iter(coefficients)
    for value in coefficients:
        if value:
            yield number_type(value)
            break
    for c in coefficients:
        yield number_type(c)
