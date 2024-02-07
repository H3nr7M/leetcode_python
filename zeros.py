from collections import Counter
#times of times you can find a word in a string
# class Solution:
#     def maxNumberOfBalloons(self, text: str) -> int:
#         countText = Counter(text)
#         balloon = Counter("balloon")
#         res = len(text) # or float("inf")
#         for c in balloon:#toma las llaves
#             res = min(res, countText[c] // balloon [c])
#         return res

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        s='balloon'
        dic={}
        res =float('inf')
        for i in s:
            dic[i]=1+dic.get(i,0)
        dic1={}
        for i in text:
            if i in dic:
                dic1[i]=1+dic1.get(i,0)
        for c in dic:
            res = min(res, dic1[c] // dic[c])
        return res


text = "loonbalxballpoon"
print(Solution().maxNumberOfBalloons(text)) # Output: 2