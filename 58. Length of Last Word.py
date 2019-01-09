"""

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""

def lengthOfLastWord( s):
    return max(map(len,s.split()))

s="hello world"
print(lengthOfLastWord( s))