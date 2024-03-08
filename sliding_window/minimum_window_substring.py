# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring
#  of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique.
# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Contador de los caracteres en la cadena t
        target_counter = Counter(t)
        # Número de caracteres únicos en la cadena t
        required_chars = len(target_counter)
        # Inicialización de variables
        left, right = 0, 0
        min_length = float('inf')
        min_window = ""
        
        # Contador de los caracteres encontrados en la ventana actual
        window_counter = Counter()
        
        # Recorrido de la cadena s
        while right < len(s):
            # Expandir la ventana hasta que se cumplan todos los caracteres requeridos
            while right < len(s) and required_chars > 0:
                char = s[right]
                window_counter[char] += 1
                # Verificar si el carácter actual se encuentra en la cadena t y si se alcanzó su frecuencia requerida
                if char in target_counter and window_counter[char] == target_counter[char]:
                    required_chars -= 1
                right += 1
            
            # Si todos los caracteres requeridos están presentes, intentar reducir la ventana
            while required_chars == 0:
                # Actualizar la longitud mínima y la subcadena mínima
                if right - left < min_length:
                    min_length = right - left
                    min_window = s[left:right]
                
                # Reducir la ventana desde el lado izquierdo
                # en el caso de que quites un caracter requerido
                char = s[left]
                if char in target_counter and window_counter[char] == target_counter[char]:
                    required_chars += 1
                window_counter[char] -= 1
                left += 1
        
        return min_window

if __name__ == "__main__":
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC")) # BANC