"""
Write a function that takes a string as input and returns the string reversed.

Example 1:

Input: "hello"
Output: "olleh"
Example 2:

Input: "A man, a plan, a canal: Panama"
Output: "amanaP :lanac a ,nalp a ,nam A"
"""
s="A man, a plan, a canal: Panama"
# # my solution
# s[::-1]

# amazing solution
length = len(s)
output = ''
while length > 0:
     length -= 1
     output += s[length]