import math

def quadratic(a, b, c):
    if not isinstance(a, (int, float)):
        raise TypeError('a bad operand type')
    if not isinstance(b, (int, float)):
        raise TypeError('b bad operand type')
    if not isinstance(c, (int, float)):
        raise TypeError('c bad operand type')
    x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
    x2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
    return x1,x2
print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))