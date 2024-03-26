'''
Given an array of integers temperatures represents the daily temperatures
, return an array answer such that answer[i] is the number of days you have
 to wait after the ith day to get a warmer temperature. If there is no 
 future day for which this is possible, keep answer[i] == 0 instead.
Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

'''
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                result[j] = i - j #utiliza los indices para sacar la diferencia de dias
            stack.append(i) #almacena indices

        return result

sol = Solution()
temperatures = [73,74,75,71,69,72,76,73]
print(sol.dailyTemperatures(temperatures=temperatures))