# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        # Inicializa los punteros izquierdo y derecho
        left, right = 0, len(s) - 1

        # Itera a través de la cadena desde ambos extremos
        while left < right:
            # Avanza el puntero izquierdo hasta encontrar un carácter alfanumérico
            while left < right and not s[left].isalnum():
                left += 1
            
            # Avanza el puntero derecho hasta encontrar un carácter alfanumérico
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compara los caracteres sin distinguir entre mayúsculas y minúsculas
            if s[left].lower() != s[right].lower():
                return False
            
            # Avanza los punteros
            left += 1
            right -= 1
        
        return True
        

s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))  # Output: True
