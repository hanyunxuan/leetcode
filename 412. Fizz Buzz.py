"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""
# my solution
n = 15
# ans=[]
# for i in range(n):
#     if (i+1)%3==0 and (i+1)%5==0:
#         ans.append('FizzBuzz')
#     elif (i+1)%3==0:
#         ans.append('Fizz')
#     elif (i+1)%5==0:
#         ans.append('Buzz')
#     else:
#         ans.append(str(i+1))
# amazing solution
a = ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) + str(i) * min(1, (i % 3)) * min(1, (i % 5)) for i in range(1, n + 1)]
b = ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]
