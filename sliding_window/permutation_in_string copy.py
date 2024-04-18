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
        if len(s1) > len(s2):
            return False

        s1_freq = [0] * 26
        s2_freq = [0] * 26

        # Calcular las frecuencias de los caracteres en s1 y la primera ventana de s2
        for i in range(len(s1)):
            s1_freq[ord(s1[i]) - ord('a')] += 1
            s2_freq[ord(s2[i]) - ord('a')] += 1

        # Comprobar si la primera ventana de s2 es una permutación de s1
        if s1_freq == s2_freq:
            return True

        # Deslizar la ventana de s2 y comprobar en cada paso
        for i in range(len(s1), len(s2)):
            # Agregar el nuevo carácter a la ventana deslizante
            s2_freq[ord(s2[i]) - ord('a')] += 1
            # Restar el carácter que sale de la ventana
            s2_freq[ord(s2[i - len(s1)]) - ord('a')] -= 1
            # Comprobar si la ventana actual es una permutación de s1
            if s1_freq == s2_freq:
                return True

        return False

    
sol = Solution()
s1 = "ab"
s2 = "eidbaooo"
print(sol.checkInclusion(s1, s2))
