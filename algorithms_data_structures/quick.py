# quick sort algorithm

def quick_sort(arr):
    if len(arr) > 1:
        pivot = arr[-1] # choose the last element as the pivot
        left = []
        right = []

        for i in range(len(arr) - 1):
            if arr[i] < pivot:
                left.append(arr[i]) # add to the left half
            else:
                right.append(arr[i]) # add to the right half

        return quick_sort(left) + [pivot] + quick_sort(right) # merge the 2 halves
    else:
        return arr
    
arr = [5, 4, 3, 2, 1]
print(quick_sort(arr))