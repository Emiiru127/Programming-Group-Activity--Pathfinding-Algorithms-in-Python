from queue import PriorityQueue
import time

def heuristic(a, b):

    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def greedy_best_first_search(grid, start, goal):

    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    visited = set()

    while not open_set.empty():
        current = open_set.get()[1]

        if current == goal:
            return reconstruct_path(came_from, current)

        visited.add(current)

        for neighbor in get_neighbors(current, grid):
            if neighbor not in visited:
                priority = heuristic(neighbor, goal)
                open_set.put((priority, neighbor))
                came_from[neighbor] = current

    return None


def a_star_search(grid, start, goal):

    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}

    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    visited = set()

    while not open_set.empty():
        current = open_set.get()[1]

        if current == goal:
            return reconstruct_path(came_from, current)

        visited.add(current)

        for neighbor in get_neighbors(current, grid):
            tentative_g_score = g_score[current] + 1

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                if neighbor not in visited:
                    open_set.put((f_score[neighbor], neighbor))

    return None


def get_neighbors(node, grid):

    x, y = node
    neighbors = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
            neighbors.append((nx, ny))
    return neighbors


def reconstruct_path(came_from, current):

    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return total_path[::-1]


if __name__ == "__main__":

    grid = [

        [0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 1, 0],

    ]

    start = (0, 0)
    goal = (4, 4)

    start_time = time.perf_counter()
    path_greedy = greedy_best_first_search(grid, start, goal)
    time_greedy = time.perf_counter() - start_time
    print("\nGreedy Best-First Search:")
    print("Path found:", path_greedy)
    print("Time taken: {:.8f} seconds".format(time_greedy))

    # Measure A* Search time
    start_time = time.perf_counter()
    path_a_star = a_star_search(grid, start, goal)
    time_a_star = time.perf_counter() - start_time
    print("\nA* Search:")
    print("Path found:", path_a_star)
    print("Time taken: {:.8f} seconds".format(time_a_star))

    # Efficiency Comparison
    print("\nEfficiency Comparison:")
    print("Greedy Best-First Search took {:.8f} seconds".format(time_greedy))
    print("A* Search took {:.8f} seconds".format(time_a_star))

    # Path Quality Comparison
    print("\nPath Quality Comparison:")
    print("Length of path found by Greedy:", len(path_greedy) if path_greedy else "No path found")
    print("Length of path found by A*:", len(path_a_star) if path_a_star else "No path found")
    print()