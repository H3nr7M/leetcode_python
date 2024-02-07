'''
Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
'''
def longest_palindromic_substring(string):
    n = len(string)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    max_length = 1
    start = 0
    for length in range(2, n+1):
        for i in range(n - length + 1):
            j = i + length - 1
            if string[i] == string[j] and (length == 2 or dp[i+1][j-1]):
                dp[i][j] = 1
                if length > max_length:
                    max_length = length
                    start = i
    return string[start:start+max_length]

# Example usage
print(longest_palindromic_substring("bananas"))
# Output: 'anana'

# The time complexity of this solution is O(n^2) and the space complexity is O(n^2).

