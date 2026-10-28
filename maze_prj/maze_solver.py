import heapq
import math

def manhattan_distance(p1, p2):
    """Calculates Manhattan distance between two points (x1, y1) and (x2, y2)."""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def euclidean_distance(p1, p2):
    """Calculates Euclidean distance between two points (x1, y1) and (x2, y2)."""
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def a_star_search(grid, start, goal, heuristic=manhattan_distance):
    """
    Executes A* Search to find the optimal path from start to goal.
    Returns path as a list of (row, col) tuples, or None if unreachable.
    """
    rows, cols = len(grid), len(grid[0])
    
    # Priority Queue stores tuples of: (f_score, counter, (row, col))
    count = 0
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), count, start))
    
    # Map to trace optimal path back to start
    came_from = {}
    
    # g_score: Cost of shortest known path from start to node
    g_score = {start: 0}
    
    # Track nodes present in the open set heap
    open_set_hash = {start}

    while open_set:
        _, _, current = heapq.heappop(open_set)
        open_set_hash.remove(current)

        # Goal check
        if current == goal:
            path = []
            curr = goal
            while curr in came_from:
                path.append(curr)
                curr = came_from[curr]
            path.append(start)
            path.reverse()
            return path

        r, c = current
        # 4-directional movement (Up, Down, Left, Right)
        neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]

        for nr, nc in neighbors:
            # Check grid bounds and ensure target cell is not a wall (1)
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                tentative_g_score = g_score[current] + 1

                if (nr, nc) not in g_score or tentative_g_score < g_score[(nr, nc)]:
                    came_from[(nr, nc)] = current
                    g_score[(nr, nc)] = tentative_g_score
                    f_score = tentative_g_score + heuristic((nr, nc), goal)

                    if (nr, nc) not in open_set_hash:
                        count += 1
                        heapq.heappush(open_set, (f_score, count, (nr, nc)))
                        open_set_hash.add((nr, nc))

    return None  # Path is blocked or goal is unreachable

def display_maze(grid, start, goal, path=None):
    """Visualizes the grid, obstacles, start, goal, and calculated path in CLI."""
    rows, cols = len(grid), len(grid[0])
    path_set = set(path) if path else set()

    print("+" + "---+" * cols)
    for r in range(rows):
        row_str = "|"
        for c in range(cols):
            cell = (r, c)
            if cell == start:
                row_str += " S |"
            elif cell == goal:
                row_str += " G |"
            elif cell in path_set:
                row_str += " * |"  # Asterisk represents optimal path
            elif grid[r][c] == 1:
                row_str += " █ |"  # Wall symbol
            else:
                row_str += "   |"
        print(row_str)
        print("+" + "---+" * cols)

if __name__ == "__main__":
    # 0 = Open path, 1 = Wall / Obstacle
    maze = [
        [0, 0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0]
    ]

    start_pos = (0, 0)
    goal_pos = (4, 5)

    print("=== A* Maze Solver ===")
    print("Initial Grid:")
    display_maze(maze, start_pos, goal_pos)

    print("\nSolving using A* (Manhattan Heuristic)...")
    optimal_path = a_star_search(maze, start_pos, goal_pos, heuristic=manhattan_distance)

    if optimal_path:
        print(f"\nPath found! Total steps: {len(optimal_path) - 1}")
        display_maze(maze, start_pos, goal_pos, optimal_path)
    else:
        print("\nNo valid path found! The goal is completely blocked.")