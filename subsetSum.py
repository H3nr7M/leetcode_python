def subset_sum(numbers, target):
    def dfs(index, target, path, res):
        if target == 0:
            res.append(path)
            return 
        if target < 0 or index == len(numbers):
            return 
        dfs(index + 1, target, path, res)
        dfs(index + 1, target - numbers[index], path + [numbers[index]], res)

    res = []
    dfs(0, target, [], res)
    return res if res else None

S = [12, 1, 61, 5, 9, 2]
k = 24
result = subset_sum(S, k)
print(result) # Output: [12, 9, 2, 1]
