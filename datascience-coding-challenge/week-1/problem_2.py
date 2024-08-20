"""PROBLEM 2
You have been given a string. You need to remove all the duplicates from the string. The final output string should contain each character only once. The respective order of the characters inside the string should remain the same. You can traverse the string only once.

Test Case 1:
Input: abaabbbacd
Output: abcd

Test Case 2:
Input: ddeefggh
Output: defgh"""

str = input()
new_str = ""
for s in str:
    if s not in new_str:
        new_str += s
print(new_str)
