# linear search algorithm

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1

arr = [5, 4, 3, 2, 1]
print(linear_search(arr, 3))

# Time complexity: O(n)
# Space complexity: O(1)