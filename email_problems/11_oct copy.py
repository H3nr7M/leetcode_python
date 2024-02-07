def leastBricks(wall):
    dic = {}
    
    for row in wall:
        lastPosition = 0
        for i in range(len(row)-1):
            lastPosition += row[i]
            if lastPosition in dic:
                dic[lastPosition] += 1
            else:
                dic[lastPosition] = 1
    maxValue = 0
    for i in dic.values():
        maxValue = max(i, maxValue)
    
    result = len(wall) - maxValue
    return result

# Example usage:
wall = [
    [1, 2, 2, 1],
    [3, 1, 2],
    [1, 3, 2],
    [2, 4],
    [3, 1, 2],
    [1, 3, 1, 1]
]

result = leastBricks(wall)
print("The fewest number of bricks crossed by a vertical line is:", result)

# hace un diccionario con el numero de ladrillos que terminan en cierta posicion y luego resta esa cantidad al numero de capas y la que resulte menor es la que regresa
