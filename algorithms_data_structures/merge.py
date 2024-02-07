# merge sort algorithm

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2 # find the middle index
        left = arr[:mid] # left half
        right = arr[mid:] # right half

        merge_sort(left) # sort the left half
        merge_sort(right) # sort the right half

        i = j = k = 0 # initialize pointers

        while i < len(left) and j < len(right): # merge the 2 halves
            if left[i] < right[j]:
                arr[k] = left[i] # update the element in the array
                i += 1
            else:
                arr[k] = right[j] # update the element in the array
                j += 1
            k += 1

        while i < len(left): # merge the left half
            arr[k] = left[i] # update the element in the array
            i += 1
            k += 1

        while j < len(right): # merge the right half
            arr[k] = right[j] # update the element in the array
            j += 1
            k += 1

    return arr

arr = [5, 4, 3, 2, 1]
print(merge_sort(arr))