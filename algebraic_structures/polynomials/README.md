# Задачи с полиномами

## `main.py`
В нём следует указать входные данные для алгоритма поиска НОД

Например, для поиска НОД многочленов x<sup>2</sup>+x и x+1 необходимо поменять
```python
p1 = Polynomial([1, 1, 0])
p2 = Ploynomial([1, 1])
```
(Коэффициент при x<sup>0</sup> равен 0)

Для работы в кольце вычетов необходимо поменять переменную NUMERIC_TYPE_FOR_COEFFICIENTS в `config.py`

## `division.py`
Алгоритм деления многочленов в столбик

## `gcd.py`
Поиск наибольшего общего делителя двух многочленов

## `config.py`
Содержит Переменные для настройки работы алгоритма
