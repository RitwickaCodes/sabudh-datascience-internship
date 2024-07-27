"""PROBLEM 9

Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

Test case 1
input = 4
output = 24

Test case 2
input = 2
output = 2"""


def factorial(n):
    fact = 1
    if n == 0:
        fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


n = int(input())
print(factorial(n))
