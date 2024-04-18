'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order. An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:
Input: strs = [""]
Output: [[""]]
'''
# import collections

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = {}
        
        for word in strs:
            sorted_s = ''.join(sorted(word))
            if sorted_s not in anagrams:
                anagrams[sorted_s] = [word]
            else:
                anagrams[sorted_s].append(word)
        
        return list(anagrams.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(strs)) #[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
