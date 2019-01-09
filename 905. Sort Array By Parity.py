"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.



Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
"""
A=[3,1,2,4]
# My solution
# A_even=[]
# A_odd=[]
# for a in A:
#     if a%2==0:
#         A_even.append(a)
#     else:
#         A_odd.append(a)
# A_new=A_even+A_odd

# My solution 2
# start=-1
# count=0
# while True:
#     count+=1
#     start+=1
#     if A[start] %2 !=0:
#         A.append(A[start])
#         A.pop(start)
#         start-=1
#     if count == len(A):
#         break

# amazing solution
start=0
end=len(A)-1
A_new=[None]*len(A)
for i in A:
    if i % 2 ==0:
        A_new[start]=i
        start+=1
    else:
        A_new[end]=i
        end-=1