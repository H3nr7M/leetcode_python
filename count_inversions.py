def count_inversions(array):
    def merge_sort(array, start, end):
        if start >= end:
            return 0
        
        mid = (start + end) // 2
        count = merge_sort(array, start, mid) + merge_sort(array, mid + 1, end)
        i, j = start, mid + 1
        while i <= mid and j <= end:
            if array[i] <= array[j]:
                i += 1
            else:
                count += mid - i + 1
                j += 1
        
        array[start:end + 1] = sorted(array[start:end + 1])
        return count
    
    return merge_sort(array, 0, len(array) - 1)

array = [2, 4, 1, 3, 5]
result = count_inversions(array)
print(result) # Output: 3
