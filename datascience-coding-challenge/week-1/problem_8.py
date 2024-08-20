"""PROBLEM 8

Write a Python program to find the median of three values.

Test case 1
 Input: 
Input first number: 15
Input second number: 26
Input third number: 29
Output : 26

Test case 2
 Input: 
Input first number: 10
Input second number: 20
Input third number: 5
Output : 10"""

my_list = []
a = int(input("Input first number:"))
my_list.append(a)
b = int(input("Input second number:"))
my_list.append(b)
c = int(input("Input third number:"))
my_list.append(c)

print(sorted(my_list)[1])
