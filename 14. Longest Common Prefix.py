"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs:
            s = strs[0]
            for i in strs[1::]:
                com = []
                count = 1
                for j in range(min(len(i), len(s))):
                    if i[j] == s[j]:
                        if count - j == 1:
                            com.append(i[j])
                            # count.append(j)
                            count += 1
                s = str(''.join(str(i) for i in com))
            return s
        else:
            return ""