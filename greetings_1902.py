# All the solutions supposed to be done without 
# using specific Python math functions.

import math
from sympy import symbols, simplify, Eq, solve

def arithmetic_remainder(num1, num2):
    trunc_num = math.trunc(num1 / num2)
    num3 = trunc_num * num2
    output = num1 - num3
    
    return output

    # Complex
        # output = num1 - math.trunc(num1 / num2) * num2
        # return print(output)
        
    # Optimized
        # return num1 % num2
    
def percentage_from(num, percent):
    return (percent / 100) * num

def rectangle_area(a, b):
    return a * b

def rectangle_hypotenuse(leg1, leg2):
    return math.sqrt(leg1**2 + leg2**2)

def sum_from_one(n):
    return n * (n + 1) // 2 # (arithmetic progression)

def algebra_simplify():
    x, y = symbols('x y')
    expression = (x + y)**2 - (x - y)**2
    simplified_expression = simplify(expression)
    return simplified_expression

def solve_equation():
    x = symbols('x')
    equation = Eq(4*x - 7, 2*x + 9)
    solution = solve(equation, x)
    return solution[0]

def main():
    # Chapter No.1
    print("Остаток от деления:", arithmetic_remainder(2023, 13))
    print("15% от 800:", percentage_from(800, 15))

    # Chapter No.2
    print("Упрощенное выражение:", algebra_simplify())
    print("Решение уравнения:", solve_equation())
    
    # Chapter No.3
    print("Площадь прямоугольника:", rectangle_area(6, 10))
    print("Гипотенуза треугольника:", rectangle_hypotenuse(5, 12))
    
    # Chapter No.4
    print("Сумма чисел от 1 до 14:", sum_from_one(14))

if __name__ == "__main__":
    main()