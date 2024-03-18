import math
import numpy as np
import sympy as sp
import numpy as np
"""
Receives 3 parameters:
    1.  a - start value.
    2.  b - end  value. 
    3.  err - value of tolerable error

Returns variables:
    1.  S - The minimum number of iterations required to reach the desired accuracy
"""


def max_steps(a, b, err):
    s = int(np.floor(- np.log2(err / (b - a)) / np.log2(2) - 1))
    return s


"""
Performs Iterative methods for Nonlinear Systems of Equations to determine the roots of the given function f
Receives 4 parameters:
    1. f - continuous function on the interval [a, b], where f (a) and f (b) have opposite signs.
    2. a - start value.
    3. b - end  value. 
    4. tol - the tolerable error , the default value will set as 1e-16

Returns variables:
    1.  c - The approximate root of the function f
"""


def bisection_method(f, a, b, tol=1e-6):
    # if np.sign(a) == np.sign(b):
    #     raise Exception("The scalars a and b do not bound a root")
    c, k = 0, 0
    steps = max_steps(a, b, tol)  # calculate the max steps possible

    print("{:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format("Iteration", "a", "b", "f(a)", "f(b)", "c", "f(c)"))

    # while the diff af a&b is not smaller than tol, and k is not greater than the max possible steps
    while abs(b - a) > tol and k <= steps:
        c = (a + b) / 2  # Calculation of the middle value

        if f(c) == 0:
            return c  # Procedure completed successfully

        if f(c) * f(a) < 0:  # if sign changed between steps
            b = c  # move forward
        else:
            a = c  # move backward

        print("{:<10} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f}".format(k, a, b, f(a), f(b), c, f(c)))
        k += 1

    return c  # return the current root
def find_all_roots(f, a, b, tol=1e-6):
    roots = []

    x_sym = sp.symbols('x')
    f_sym = f(x_sym)

    intervals = np.linspace(a, b, 1000000)

    for i in range(len(intervals) - 1):
        start = intervals[i]
        end = intervals[i + 1]

        if f(start) * f(end) < 0:
            try:
                root = sp.nsolve(f_sym, (start + end) / 2, tol=tol)
                roots.append(float(root))
            except ValueError:
                pass

    return roots




if __name__ == '__main__':
    f = lambda x: (6*x**6 - 7 * x ** 5 - 3)/(2*x**3 + 1)

    # Adjust the interval to avoid the singularity
    a = -2
    b = 2

    roots = find_all_roots(f, a, b)
    print(f"\nThe equation f(x) has approximate roots at {roots}")