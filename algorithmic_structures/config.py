from fractions import Fraction


class Config:
    """Класс с настройками программы"""
    """Показывать ли вычисления в столбик"""
    SHOW_INTERMEDIATE_CALCULATIONS = False
    """Заменять ли -1x на -x
    Плохо ведёт себя в кольцах вычета"""
    REPLACE_MINUS_ONE_X = False
    """Тип коэффициентов
    Например для колец вычетов может быть равен mod5 
    """
    NUMERIC_TYPE_FOR_COEFFICIENTS = Fraction
