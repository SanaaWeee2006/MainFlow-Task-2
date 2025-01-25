import random

def generate_maze(rows, cols):
    # Initialize maze with walls
    maze = [[1 for _ in range(cols)] for _ in range(rows)]

    def carve_path(x, y):
        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 < nx < rows and 0 < ny < cols and maze[nx][ny] == 1:
                # Carve the path
                maze[x + dx // 2][y + dy // 2] = 0
                maze[nx][ny] = 0
                carve_path(nx, ny)

    # Start from (1, 1)
    maze[1][1] = 0
    carve_path(1, 1)
    return maze

def solve_maze(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    stack = [start]
    visited = set()
    visited.add(start)
    parent = {start: None}

    while stack:
        x, y = stack.pop()
        if (x, y) == end:
            break
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0 and (nx, ny) not in visited:
                stack.append((nx, ny))
                visited.add((nx, ny))
                parent[(nx, ny)] = (x, y)

    # Trace the path
    path = []
    current = end
    while current:
        path.append(current)
        current = parent[current]
    path.reverse()
    return path

def display_maze(maze, path=None):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if path and (i, j) in path:
                print("·", end=" ")  # Mark path
            elif maze[i][j] == 1:
                print("█", end=" ")  # Wall
            else:
                print(" ", end=" ")  # Path
        print()

# Main Program
rows, cols = 11, 11  # Maze size (must be odd for proper path carving)
maze = generate_maze(rows, cols)
start = (1, 1)
end = (rows - 2, cols - 2)

# Solve the maze
path = solve_maze(maze, start, end)

# Display the maze
print("Generated Maze:")
display_maze(maze)

print("\nSolved Maze:")
display_maze(maze, path)
