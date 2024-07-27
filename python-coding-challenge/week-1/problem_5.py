"""PROBLEM 5

Write a program to calculate the sum of series up to n term. For example, if n = 5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690

Test Case 1:
Input : 5
Output : 24690

Test Case 2:
Input: 6
Output: 246912"""

n = int(input())
term = 0
result = 0
for i in range(n):
    term += 2 * 10**i
    result += term
print(result)
