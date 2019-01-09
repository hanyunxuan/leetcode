"""
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

Example 1:

Input: "Hello"
Output: "hello"
Example 2:

Input: "here"
Output: "here"
Example 3:

Input: "LOVELY"
Output: "lovely"
"""
str="Hello"
# My solution
output=str.lower()

# Amazing solution
"".join(chr(ord(c) + 32) if "A" <= c <= "Z" else c for c in str)