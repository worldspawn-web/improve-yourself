# All the solutions supposed to be done without 
# using specific Python math functions.

import math

def arithmetic_remainder(num1, num2):
    trunc_num = math.trunc(num1 / num2)
    num3 = trunc_num * num2
    output = num1 - num3
    
    return print(output)

    # Complex
        # output = num1 - math.trunc(num1 / num2) * num2
        # return print(output)
        
    # Optimized
        #
    
def percentage_from(num, percent):
    return print(math.trunc(num * percent / 100))

def rectangle_area(a, b):
    return print(a * b)

def rectangle_hypotenuse(leg1, leg2):
    squareHypotenuse = (leg1 * leg1) + (leg2 * leg2)
    return print(math.trunc(math.sqrt(squareHypotenuse)))

def sum_from_one(n):
    sum = 1
    for i in range(n):
        sum += i
    return print(sum)

def main():
    # Chapter No.1
    arithmetic_remainder(2023, 13)
    percentage_from(800, 15)

    # Chapter No.2
    # original_sentence = "(x + y)^2 - (x - y)^2"
    # simplified_sentence = "x^2 + 2xy + y^2 - x^2 - 2xy + y^2"
    print("2y^2")
    
    # original_sentence_2 = "4x - 7 = 2x + 9"
    # simplified_sentence_2 = "4x - 2x = 9 + 7" = "2x = 16"
    print("x = 8")
    
    # Chapter No.3
    rectangle_area(6, 10)
    rectangle_hypotenuse(5, 12)
    
    # Chapter No.4
    sum_from_one(5)

if __name__ == "__main__":
    main()