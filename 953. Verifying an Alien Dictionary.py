"""
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.



Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
"""

words = ["hello","leetcode","ahhd"]
order = "hlabcdefgijkmnopqrstuvwxyz"


# my solution
for i in range(len(words) - 1):
    word1 = words[i]
    word2 = words[i + 1]
    if len(word1) >= len(word2):
        for j in range(len(word1)):
            num1 = order.index(word1[j])
            if j + 1 > len(word2):
                num2 = 0
            else:
                num2 = order.index(word2[j])
            if num1 > num2:
                print(False)
            elif num1 == num2:
                continue
            else:
                break
    else:
        for j in range(len(word2)):
            num2 = order.index(word2[j])
            if j + 1 > len(word1):
                num1 = 0
            else:
                num1 = order.index(word1[j])
            if num1 > num2:
                print(False)
            elif num1 == num2:
                continue
            else:
                break
print(True)

# amazing solution
order_dict={x:i for i,x in enumerate(order,1)}
words=[[order_dict[w] for w in word]for word in words]
return all(w1<=w2 for w1,w2 in zip(words,words[1:]))