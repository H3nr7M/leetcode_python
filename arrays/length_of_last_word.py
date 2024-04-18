'''
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Dividir la cadena en palabras y eliminar los espacios en blanco alrededor
        words = s.split()
        # words = s.strip().split()
        
        # Verificar si hay palabras después de eliminar espacios
        if words:
            return len(words[-1])
        else:
            return 0  # Si la cadena está vacía o solo contiene espacios en blanco, la longitud de la última palabra es 0

sol = Solution()
s = "   fly me   to   the moon  "
print(sol.lengthOfLastWord(s))