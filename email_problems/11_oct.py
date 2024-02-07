
def leastBricks(wall):
    # Create a dictionary to count the positions where bricks end
    position_count = {}
    
    # Iterate through each row of the wall
    for row in wall:
        position = 0
        # Exclude the last brick's ending position
        for i in range(len(row) - 1):
            position += row[i]
            if position in position_count:
                position_count[position] += 1
            else:
                position_count[position] = 1

    # Find the maximum count of positions
    max_count = 0
    for position in position_count.values():
        max_count = max(max_count, position)
    
    # Calculate the number of bricks crossed by the vertical line
    return len(wall) - max_count

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
