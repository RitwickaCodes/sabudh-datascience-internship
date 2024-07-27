"""PROBLEM 6

Write a program to Reverse below given numbers without slicing

Test Case 1:
Input: 745633
Output: 336547

Test Case 2:
Input: 65346
Output: 64356"""

n = int(input())
reversed_no = 0
while n > 0:
    rem = n % 10
    reversed_no = reversed_no * 10 + rem
    n //= 10
print(reversed_no)
