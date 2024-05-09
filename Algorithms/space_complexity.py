import time
import random
import sys


# Function to measure the space used by a function
def space_used(func, *args):
    before_space = sys.getsizeof(func(*args))
    return before_space


# Title
print("=" * 40)
print("Space Complexity Analysis in Python")
print("=" * 40)


# O(1) - Constant Space Complexity
def constant_space_complexity():
    x = 1


constant_space = space_used(constant_space_complexity)
print("O(1) - Constant Space Complexity:", constant_space)


# O(n) - Linear Space Complexity
def linear_space_complexity(n):
    lst = list(range(n))


linear_space = space_used(linear_space_complexity, 100000)
print("O(n) - Linear Space Complexity:", linear_space)


# O(n^2) - Quadratic Space Complexity
def quadratic_space_complexity(n):
    matrix = [[0] * n for _ in range(n)]


quadratic_space = space_used(quadratic_space_complexity, 500)
print("O(n^2) - Quadratic Space Complexity:", quadratic_space)


# O(2^n) - Exponential Space Complexity (Recursive Fibonacci)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


exponential_space = space_used(fibonacci, 20)
print("O(2^n) - Exponential Space Complexity (Recursive Fibonacci):", exponential_space)
