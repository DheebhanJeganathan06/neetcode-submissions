class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        q = deque([(0, 0, 1)]) # r, c, length
        visited = set((0, 0))
        direct = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, 1], [-1, -1], [1, -1]]

        while q:
            r, c, l = q.popleft()
            if min(r, c) < 0 or max(r, c) >= len(grid) or (grid[r][c]):
                 continue
            if r == (len(grid) - 1) and c == (len(grid) - 1):
                return l
            for dr, dc in direct:
                if (r + dr, c + dc) not in visited:
                    q.append((r + dr, c + dc, l + 1)) 
                    visited.add((r + dr, c + dc))

        return -1
        