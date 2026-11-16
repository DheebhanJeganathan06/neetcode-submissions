from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
		    # if we have an invalid grid, then implicitly there are zero islands
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        # visited set to not retraverse land that's already part of an island
        visited = set()
        # islands counter for eventual return
        islands = 0
        # all possible direction lists for easy traversal
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

				# bfs helper for recursive implementation from each cell
        def bfs(r, c):
		        # initialize new queue for current "island"
            q = deque()
            # add start of island to already visited so we don't retraverse
            # and end up in an infinite loops
            visited.add((r, c))
            # add start of island to queue
            q.append((r, c))

						# breadth-first-search implementation while queue is non-empty
            while q:
                row, col = q.popleft()
                # iterate over all possible "adjacent" traversable cells
                for dr, dc in dirs:
		                # check bounds conditions and that adjacent cell is unvisited
                    if (
                        (row + dr) in range(rows)
                        and (col + dc) in range(cols)
                        and grid[row + dr][col + dc] == "1"
                        and (row + dr, col + dc) not in visited
                    ):
                    # if it is valid and unvisited, add it to queue and
                    # mark it as visited
                        q.append((row + dr, col + dc))
                        visited.add((row + dr, col + dc))

				# iterate over each cell
        for r in range(rows):
            for c in range(cols):
		            # only trigger the bfs iteration if the current cell isn't visited
		            # this will ensure we never retraverse the same island
		            # therefore, we can increment island each time bfs is called
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

				# after all cells have been traversed, we can return our islands count
        return islands