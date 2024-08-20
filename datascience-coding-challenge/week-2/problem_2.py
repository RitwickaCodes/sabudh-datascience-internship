"""Problem 2: 
Given an array of positive and negative numbers, arrange them such that all negative integers appear before all the positive integers in the array without using any additional data structure like a hash table, arrays, etc. 
The order of appearance should be maintained.

Test case 1:
Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
Output: -12 -13 -5 -7 -3 -6 11 6 5

Test case 2:
Input: -12, 11, 13, -5, 6, -7, 5, -3, 8
Output: -12 -5 -7 -3 11 13 6 5 8"""


def rearrange(arr):
    n = len(arr)
    j = 0
    for i in range(0, n):
        if arr[i] < 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return arr


# Test cases
print(rearrange([-12, 11, -13, -5, 6, -7, 5, -3, -6]))
print(rearrange([-12, 11, 13, -5, 6, -7, 5, -3, 8]))
