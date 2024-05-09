import time
import random


# Function to measure the time taken by a function
def time_function(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    return end_time - start_time


# Title
print("=" * 40)
print("Time Complexity Analysis in Python")
print("=" * 40)


# O(1) - Constant Time Complexity
def constant_time_complexity():
    x = 1


constant_time = time_function(constant_time_complexity)
print("O(1) - Constant Time Complexity:", constant_time)


# O(log n) - Logarithmic Time Complexity
def logarithmic_time_complexity(n):
    while n > 1:
        n //= 2


logarithmic_time = time_function(logarithmic_time_complexity, 100000)
print("O(log n) - Logarithmic Time Complexity:", logarithmic_time)


# O(n) - Linear Time Complexity
def linear_time_complexity(n):
    total = 0
    for i in range(n):
        total += i


linear_time = time_function(linear_time_complexity, 100000)
print("O(n) - Linear Time Complexity:", linear_time)


# O(n^2) - Quadratic Time Complexity
def quadratic_time_complexity(n):
    total = 0
    for i in range(n):
        for j in range(n):
            total += i * j


quadratic_time = time_function(quadratic_time_complexity, 500)
print("O(n^2) - Quadratic Time Complexity:", quadratic_time)


# O(2^n) - Exponential Time Complexity (Recursive Fibonacci)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


exponential_time = time_function(fibonacci, 20)
print("O(2^n) - Exponential Time Complexity (Recursive Fibonacci):", exponential_time)
