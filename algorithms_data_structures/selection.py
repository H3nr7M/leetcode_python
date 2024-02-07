# Selection sort algorithm implementation
# find the smallest element and swap it with the first element

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)): # find the smallest element
            if arr[min_index] > arr[j]:
                min_index = j # update the index of the smallest element

        arr[i], arr[min_index] = arr[min_index], arr[i] # swap the smallest element with the first element

    return arr

arr = [5, 4, 3, 2, 1]
print(selection_sort(arr))