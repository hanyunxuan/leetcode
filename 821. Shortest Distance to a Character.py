"""
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
"""
# # my solution
# S = "loveleetcode"
# C = 'e'
# indices = [i for i, x in enumerate(S) if x == C]
# Output=[]
# for i in range(len(S)):
#     Output.append(min([abs(i-s) for s in indices]))

# # amazing solution
# S = "loveleetcode"
# C = 'e'
# n = len(S)
# res = [0 if c == C else n for c in S]
# # for i in range(n - 1): res[i + 1] = min(res[i + 1], res[i] + 1)
# # for i in range(n - 1)[::-1]: res[i] = min(res[i], res[i + 1] + 1)
#
# for i in range(n - 1):
#     res[i + 1] = min(res[i + 1], res[i] + 1)
#
# for i in range(n - 1)[::-1]:
#     res[i] = min(res[i], res[i + 1] + 1)

S = "loveleetcode"
C = 'e'
Output=[len(S)  if s!=C else 0 for s in S]
for i in range(len(Output)-1):
    Output[i + 1]=min(Output[i + 1],Output[i]+ 1)

for i in range(len(Output)-1)[::-1]:
    Output[i]=min(Output[i],Output[i+1]+1)