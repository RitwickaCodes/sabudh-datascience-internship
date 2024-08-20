"""Problem 3:  
Given an array of N integers and a number K, 
the task is to find the number of pairs of integers in the array whose sum is equal to K.

Test Case 1:
Input: arr[] = {1, 5, 7, -1}, sum = 6
Output: 2
Explanation: Pairs with sum 6 are (1, 5) and (7, -1).

Test Case 2:
Input: arr[] = {1, 5, 7, -1, 5}, sum = 6
Output: 3
Explanation: Pairs with sum 6 are (1, 5), (7, -1) & (1, 5)."""


def getPairsCount(arr, sum):
    m = {}
    count = 0
    for num in arr:
        if sum - num in m:
            count += m[sum - num]
        m[num] = m.get(num, 0) + 1
    return count


# Test cases
print(getPairsCount([1, 5, 7, -1], 6))
print(getPairsCount([1, 5, 7, -1, 5], 6))
