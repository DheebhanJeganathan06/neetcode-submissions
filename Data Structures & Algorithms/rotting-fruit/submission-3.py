class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def bfs(i, j):
            new_rotted = set()
            for add_i, add_j in directions:
                new_i = i + add_i
                new_j = j + add_j

                if (new_i in range(len(grid))) and (new_j in range(len(grid[0]))) and grid[new_i][new_j] == 1:
                    new_rotted.add((new_i, new_j))
        
            return new_rotted

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count += 1

        minutes = 0
        while count > 0:
            newly_rotted = set()
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 2:
                        newly_rotted.update(bfs(i, j))

            if not newly_rotted:
                return -1

            for new_i, new_j in newly_rotted:
                grid[new_i][new_j] = 2
                count -= 1
            minutes += 1
        
        return minutes





        return minutes
        
