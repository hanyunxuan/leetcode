"""
Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
"""
nums=[1,4,3,2]
# my solution1
nums.sort()
sum=0
for i in range(0,len(nums),2):
    sum+=nums[i]
# my solution2
# sum([nums[i] for i in range(0,len(nums),2)])

# amazing solution
sum(sorted(nums)[::2])