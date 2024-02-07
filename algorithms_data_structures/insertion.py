# insertion sort algorithm

def insertion_sort(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]: # swap 2 elements
            arr[j - 1], arr[j] = arr[j], arr[j - 1] # swap
            j -= 1

    return arr

arr = [5, 4, 3, 2, 1]
print(insertion_sort(arr))

# Time complexity: O(n^2)
# Space complexity: O(1)