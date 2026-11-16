from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]):
		    # queue for bfs
        q = deque()

				# count current # of fresh oranges at time = 0
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                # also add rotten oranges to our queue
                elif grid[i][j] == 2:
                    q.append((i, j))

				# dirs list for all possible movement to adjacent cells
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        # tracks current time variable for eventual return
        time = 0

				# iterate while we have rotten AND fresh oranges
				# if we only have rotten, we're done
				# if we only have fresh, there's no way to rot it
				# at each iteration, we will only have NEWLY rotted oranges
        while q and fresh:
		        # we iterate over all values currently in our rotten queue
            for _ in range(len(q)):
                i, j = q.popleft()

								# iterate over all adjacent cells
                for plusI, plusJ in dirs:

										# if the adjacent cell is invalid skip it
                    if (i + plusI) not in range(len(grid)) or (j + plusJ) not in range(len(grid[0])):
                        continue

										# if the adjacent cell is fresh, immediately rot it
										# decrement fresh accordingly
										# append the newly rotted oranges to queue
                    if grid[i + plusI][j + plusJ] == 1:
                        grid[i + plusI][j + plusJ] = 2
                        fresh -= 1
                        q.append((i + plusI, j + plusJ))
						# after each iteration, time is incremented by 1
            time += 1
           
	      # if we have no more rotten AND fresh, we return time
	      # if we still have some fresh, then -1 because there's no way to rot it 
        return time if fresh == 0 else -1