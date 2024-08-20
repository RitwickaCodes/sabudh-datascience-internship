"""Problem 4: 
Given an array of N integers where each value represents the number of chocolates in a packet. 
Each packet can have a variable number of chocolates. 
There are m students, the task is to distribute chocolate packets such that:
Each student gets one packet.
The difference between the number of chocolates in the packet with maximum chocolates and the packet with minimum chocolates given to the students is Minimum.
 
Test Case  1
Input: arr[] = {7, 3, 2, 4, 9, 12, 56}, m = 3
Output: Minimum Difference is 2

Explanation:
We have seven packets of chocolates and we need to pick three packets for 3 students. 
If we pick 2, 3, and 4, we get the minimum difference between maximum and minimum packet sizes.

Test Case 2
Input: arr[] = {3, 4, 1, 9, 56, 7, 9, 12}, m = 5
Output: Minimum Difference is 6"""


def findMinDiff(arr, n, m):
    if m == 0 or n == 0:
        return 0
    arr.sort()
    if n < m:
        return -1
    min_diff = float("inf")
    for i in range(n - m + 1):
        diff = arr[i + m - 1] - arr[i]
        if diff < min_diff:
            min_diff = diff
    return min_diff


# Test cases
print(findMinDiff([7, 3, 2, 4, 9, 12, 56], 7, 3))
print(findMinDiff([3, 4, 1, 9, 56, 7, 9, 12], 8, 5))
