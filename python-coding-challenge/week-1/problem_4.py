"""PROBLEM 4
Write a program to count the total number of digits in a number using a while loop

Test Case 1:
Input: 75869
Output: 5

Test Case 2:
Input: 654
Output: 3"""

n = int(input())
i = 0
while n > 0:
    n //= 10
    i += 1
print(i)
