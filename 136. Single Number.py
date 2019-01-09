"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""

nums=[4,1,2,1,2]

# # my solution
# import collections
# nums_counter=collections.Counter(nums)
# for key in nums_counter:
#     if nums_counter[key]==1:
#         Output=key
# my solution 2
# nums_copy=nums
# for num in nums:
#     nums_copy.remove(num)
#     if num not in nums_copy:
#         print(num)
#         break
# # amazing solution 1
# res = 0
# for num in nums:
#     res ^= num

# # amazing solution 2
# 2*sum(set(nums))-sum(nums)

# # amazing solution 3
# from functools import reduce
#
# reduce((lambda x,y:x^y),nums)