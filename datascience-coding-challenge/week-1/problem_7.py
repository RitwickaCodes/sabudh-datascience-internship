"""PROBLEM  7

Write a program to Use a loop to display elements from a given list present at odd index position

Test Case 1:
Input: 10, 20, 30, 40, 50, 60, 70, 80, 90, 100
Output: [20, 40, 60, 80, 100]

Test Case 2:
Input: 23, 46, 69, 92, 115
Output: [46, 92] """

n = input()
input_list = [int(i) for i in n.split(",")]
output_list = []
for i, x in enumerate(input_list):
    if i % 2 != 0:
        output_list.append(x)

print(output_list)
