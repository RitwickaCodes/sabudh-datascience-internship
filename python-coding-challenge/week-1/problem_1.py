"""PROBLEM 1
Read an integer N. For all non-negative integers i < N, print i^2. 

Test Case 1
Input: 5
Output :  [0, 1, 4, 9, 16]

Test Case 2
Input: 4
Output: [0, 1, 4, 9]"""

N = int(input())
my_list = []
for i in range(N):
    my_list.append(i**2)
print(my_list)
