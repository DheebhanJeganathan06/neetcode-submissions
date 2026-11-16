class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def bfs(i, j):
            if grid[i][j] == 0 or (i,j) in visited:
                return 0

            visited.add((i,j))
            count = 0
            for plusI, plusJ in directions:
                newI, newJ = i + plusI, j + plusJ
                if newI in range(len(grid)) and newJ in range(len(grid[0])):
                    count += bfs(newI, newJ)
            return 1 + count
            



        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    maxArea = max(maxArea, bfs(i,j))

        return maxArea
        