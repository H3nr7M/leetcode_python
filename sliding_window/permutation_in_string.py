'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dic = {}
        s2_dic = {}
        slices = len(s1)

        for char in s1:
            s1_dic[char] = s1_dic.get(char, 0) + 1

        #interacion es quitar y poner a un diccionario
        for i in range(len(s2)):
            if s2[i] in s1_dic and i+slices-1 < len(s2):
                for j in range(slices):
                    s2_dic[s2[i+j]] = s2_dic.get(s2[i+j], 0) + 1

                if s2_dic == s1_dic:
                    return True
                else:
                    s2_dic.clear()

        return False
    
sol = Solution()
s1 = "ab"
s2 = "eidbaooo"
print(sol.checkInclusion(s1, s2))
