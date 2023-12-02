from algebraic_structures.polynomials.algorithms.gcd import polynomial_gcd
from algebraic_structures.polynomials.structures.modulo import Modulo, mod5
from algebraic_structures.polynomials.structures.polynomial import Polynomial

# p1 = Polynomial([1, 3, -1, -4, -3])  # Correct. It is x + 3
# p2 = Polynomial([3, 10, 2, -3])
p1 = Polynomial([1, -1, -3])  # Correct. It is 1
p2 = Polynomial([1, 1])
# p1 = Polynomial([1, 3, 3, 2])  # Correct. It is x^2 + x + 1
# p2 = Polynomial([1, 2, 2, 1])
# p1 = Polynomial([1, 1, -1, -3, -3, -1])  # Correct. It is x^2 + x + 1
# p2 = Polynomial([1, -2, -1, -2, 1])
# p1 = Polynomial([3, 0, 3, 3, 0, 2, 4], number_type=mod5)  # Correct. It is x^2 + x + 1
# p2 = Polynomial([2, 3, 3, 3, 3, 3, 1], number_type=mod5)

print(f'Ответ: {polynomial_gcd(p1, p2).normalize()}')
