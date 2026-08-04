class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh.append((i, j))
        
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        time = 0
        while fresh:
            possible = False
            newRotten = []
            for i, j in fresh:
                
                # check in every direction from current fresh fruit
                for plusI, plusJ in dirs:
                    # ensure potential cell is valid
                    if min(i + plusI, j + plusJ) < 0 or (i + plusI) >= len(grid) or (j + plusJ) >= len(grid[0]):
                        continue
                    # check if adjacent fruit is rotten; if it is, rot current fruit and remove from fresh
                    if grid[i + plusI][j + plusJ] == 2:
                        newRotten.append((i, j))
                        possible = True
                        break

            if not possible:
                return -1

            for i, j in newRotten:
                fresh.remove((i, j))
                grid[i][j] = 2

            time += 1
        return time


        