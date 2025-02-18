# Theory
import math

import matplotlib.pyplot as plt
import numpy as np

def solve_quadratic(a, b, c):
    
    # Пример:
    # ax**2 + b*x + c = 0
    
    if a == 0:
        return "Это не квадратное уравнение!"
    
    # Вычисляем дискриминант
    D = b**2 - 4*a*c
    
    # Проверка наличия дискриминанта
    if D > 0:
        root1 = (-b + math.sqrt(D)) / (2 * a)
        root2 = (-b - math.sqrt(D)) / (2 * a)
        return root1, root2
    elif D == 0:
        root = -b / (2 * a)
        return root
    else:
        return "Нет действительных корней!"
    
def graph_build():
    # y = x**2 - 4*x + 3
    
    def f(x):
        return x**2 - 4*x + 3
    
    x = np.linspace(-1 , -5, 400)
    y = f(x)
    
    plt.plot(x, y, label = "y = x^2 - 4x + 3")
    plt.axhline(0, color = "black", linewidth = 0.5)
    plt.axvline(0, color = "black", linewidth = 0.5)
    plt.grid(color = "gray", linestyle = "--", linewidth = 0.5)
    plt.legend()
    plt.title("График функции")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

def main():
    # №1 - Квадратные уравнения
    print("Корни квадратного уравнения, где D > 0: ", solve_quadratic(1, -3, 2))
    print("Корни квадратного уравнения, где D = 0: ", solve_quadratic(1, 2, 1))
    print("Корни квадратного уравнения, где D < 0: ", solve_quadratic(1, 1, 1))
    
    # №2 - Графики функций
    graph_build()
    
    # №3 - 
    
if __name__ == "__main__":
    main()