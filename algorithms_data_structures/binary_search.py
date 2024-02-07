# binary search algorithm

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

arr = [5, 4, 3, 2, 1]
print(binary_search(arr, 3))

# Time complexity: O(log(n))
# Space complexity: O(1)