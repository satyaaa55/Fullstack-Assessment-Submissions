import sys
from collections import deque

def minMinutesToRot(grid):
    rows = len(grid)
    cols = len(grid[0])
    queue = deque()
    fresh = 0

    # Step 1: find all rotten, count all fresh
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            if grid[r][c] == 1:
                fresh += 1

    # No fresh oranges at all
    if fresh == 0:
        return 0

    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    minutes = 0

    # Step 2: BFS from all rotten oranges simultaneously
    while queue and fresh > 0:
        size = len(queue)
        for _ in range(size):
            r, c = queue.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))
        minutes += 1

    # Step 3: if fresh still > 0, some oranges unreachable
    return minutes if fresh == 0 else -1

if __name__ == '__main__':
    gridRows = int(input().strip())
    gridColumns = int(input().strip())

    grid = []
    for _ in range(gridRows):
        grid.append(list(map(int, input().strip().split())))

    result = minMinutesToRot(grid)
    print(result)