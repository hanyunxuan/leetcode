"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.

Cannot understand the problem
"""


def removeDuplicates( A):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not A:
        return 0

    newTail = 0

    for i in range(1, len(A)):
        if A[i] != A[newTail]:
            newTail += 1
            A[newTail] = A[i]

    return newTail + 1


A = [1,2,2,3,3,4]
print(removeDuplicates(A ))
