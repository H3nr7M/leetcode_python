# Bubble sort algorithm implementation
# swap adjacent elements if they are in wrong order

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j + 1] < arr[j]: # swap 2 elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # swap

    return arr
    

arr = [5, 4, 3, 2, 1]
print(bubble_sort(arr))

# Time complexity: O(n^2)
# Space complexity: O(1)