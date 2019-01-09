"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.

"""

x=[0, 0, 0, 1]
y=[0, 1, 0, 0]
sum(x[i] != y[i] for i in range(len(x)))

# ^是按位异或逻辑运算符，比如5^6，其实是101^110，结果是011，所以5^6的答案是3
x=1
y=4

bin(x^y).count('1')