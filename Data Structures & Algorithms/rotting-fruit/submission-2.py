from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]):
        q = deque()

        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        time = 0

        while q and fresh:
            for _ in range(len(q)):

                i, j = q.popleft()

                for plusI, plusJ in dirs:

                    if min(i + plusI, j + plusJ) < 0 or \
                       i + plusI >= len(grid) or \
                       j + plusJ >= len(grid[0]):
                        continue

                    if grid[i + plusI][j + plusJ] == 1:
                        grid[i + plusI][j + plusJ] = 2
                        fresh -= 1
                        q.append((i + plusI, j + plusJ))

            time += 1
            
        return time if fresh == 0 else -1