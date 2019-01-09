"""
Given two integers L and R, find the count of numbers in the range [L, R] (inclusive) having a prime number of set bits in their binary representation.

(Recall that the number of set bits an integer has is the number of 1s present when written in binary. For example, 21 written in binary is 10101 which has 3 set bits. Also, 1 is not a prime.)

Example 1:

Input: L = 6, R = 10
Output: 4
Explanation:
6 -> 110 (2 set bits, 2 is prime)
7 -> 111 (3 set bits, 3 is prime)
9 -> 1001 (2 set bits , 2 is prime)
10->1010 (2 set bits , 2 is prime)
Example 2:

Input: L = 10, R = 15
Output: 5
Explanation:
10 -> 1010 (2 set bits, 2 is prime)
11 -> 1011 (3 set bits, 3 is prime)
12 -> 1100 (2 set bits, 2 is prime)
13 -> 1101 (3 set bits, 3 is prime)
14 -> 1110 (3 set bits, 3 is prime)
15 -> 1111 (4 set bits, 4 is not prime)

"""
L = 6
R = 10
# my solution
# convert number to binary
# counter sum of one
# judge prime
count = 0
for i in range(L, R + 1):
    num = sum(list(map(int, bin(i)[2:len(bin(i))])))
    # judge prime
    if num == 2:
        count += 1
    elif num > 2:
        count += 1
        for j in range(2, num):
            if num % j == 0:
                count -= 1
                break

# amazing solution
sum(665772>>bin(i).count('1')&1 for i in range(L,R+1))

# convert number to binary
# counter sum of one
bin(number).count('1')

# judge prime
665772>>number &1