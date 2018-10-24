"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return False if x<0 else x == int(str(x)[::-1])
        dict = {"(": 1, ")": -1, "[": 2, "]": -2, "{": 1, "}": 1, }
        count = 0
        num = ""
        for i in range(len(s)):
            count += dict[s[i]]
            num += str(abs(dict[s[i]]))
            if count == 0:
                num = ""
                if num == num[::-1]:
                    output = True
                else:
                    return False