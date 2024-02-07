# Run-length encoding is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "aabccc" we replace "aa" by "a2" and replace "ccc" by "c3". Thus the compressed string becomes "a2bc3".

# Notice that in this problem, we are not adding '1' after single characters.

# Given a string s and an integer k. You need to delete at most k characters from s such that the run-length encoded version of s has minimum length.

# Find the minimum length of the run-length encoded version of s after deleting at most k characters.



def minLengthEncoding(s, k):
    n = len(s)
    # Initialize a list to store the length of each run
    run_length = [1] * n
    for i in range(n - 2, -1, -1):
        # Check if the current character is the same as the next character
        if s[i] == s[i + 1]:
            # If so, increment the run length of the current character
            run_length[i] = run_length[i + 1] + 1
    # Sort the runs in decreasing order of length
    run_length.sort(reverse=True)
    # Initialize the number of deletions needed
    deletions = 0
    # Iterate through the runs
    for i in range(n):
        # If the current run length is greater than 1
        if run_length[i] > 1:
            # Check if the number of deletions needed to change the current run into a shorter run is less than k
            if (run_length[i] - 1) * run_length[i] // 2 <= k:
                # If so, increment the number of deletions by the number of deletions needed
                deletions += (run_length[i] - 1) * run_length[i] // 2
                # Decrement k by the number of deletions
                k -= (run_length[i] - 1) * run_length[i] // 2
            else:
                # If not, break the loop
                break
    # Return the length of the run-length encoded version of s after deleting at most k characters
    return n - deletions

# Time complexity: O(nlogn)
# Space complexity: O(n)

s="aabccc"
k=2
print(minLengthEncoding(s,k))
