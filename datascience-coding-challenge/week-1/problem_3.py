"""PROBLEM 3
Write a program to display only those numbers from a list that satisfy the following conditions

The number must be divisible by five
If the number is greater than 150, then skip it and move to the next number
If the number is greater than 500, then stop the loop
 
Test Case 1:
Input : 12, 75, 150, 180, 145, 525, 50
Output : [75, 150, 145]

Test Case 2:
Input : 14, 85, 625, 75
Output : [85]"""

n = input()
input_list = [int(i) for i in n.split(",")]
output_list = []
for i in input_list:
    if i > 500:
        break
    if i % 5 == 0:
        if i > 150:
            continue
        output_list.append(i)

print(output_list)
