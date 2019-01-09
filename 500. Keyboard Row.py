"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

Example:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
"""
# my solution
words = ["asdfghjkl","qwertyuiop","zxcvbnm"]
# Output = []
# alphabet_dict = {'q': 1, 'w': 1, 'e': 1, 'r': 1, 't': 1, 'y': 1, 'u': 1, 'i': 1, 'o': 1, 'p': 1,
#                  'a': 2, 's': 2, 'd': 2, 'f': 2, 'g': 2, 'h': 2, 'j': 2, 'k': 2, 'l': 2,
#                  'z': 3, 'x': 3, 'c': 3, 'v': 3, 'b': 3, 'n': 3, 'm': 3}
# for word in words:
#     Output.append(word)
#     for w in range(len(list(word)) - 1):
#         alphaber1 = list(word)[w].lower()
#         alphaber2 = list(word)[w + 1].lower()
#         if alphabet_dict[alphaber1] != alphabet_dict[alphaber2]:
#             Output.remove(word)
#             break
# amazing solution1
import re
a=filter(re.compile('(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$').match, words)
# # amazing solution2
# a = set('qwertyuiop')
# b = set('asdfghjkl')
# c = set('zxcvbnm')
# ans = []
# for word in words:
#     t = set(word.lower())
#     if a & t == t:
#         ans.append(word)
#     if b & t == t:
#         ans.append(word)
#     if c & t == t:
#         ans.append(word)
