'''
Given n pairs of parentheses, write a function 
to generate all combinations of well-formed parentheses.
Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:
Input: n = 1
Output: ["()"]
En una permutación, el orden de los elementos es importante
Por ejemplo, si tienes los elementos [1, 2, 3] y quieres todas las permutaciones de longitud 2, 
obtendrías [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)].
En una combinación, el orden de los elementos no es importante
Por ejemplo, si tienes los elementos [1, 2, 3] y quieres todas las combinaciones de longitud 2, 
obtendrías [(1, 2), (1, 3), (2, 3)].
'''
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def backtrack(s='', left=0, right=0):
            if len(s) == 2 * n: #numero de simbolos
                result.append(s)
                return

            if left < n: #importante poner left antes
                backtrack(s + '(', left + 1, right)

            if right < left:
                backtrack(s + ')', left, right + 1)

        result = []
        backtrack()
        return result

# Ejemplo de uso:
sol = Solution()
n = 3
print(sol.generateParenthesis(n))