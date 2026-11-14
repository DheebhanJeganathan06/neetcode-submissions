class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(i, j, index, seen):

            if (i, j) in seen:
                return False

            if board[i][j] != word[index]:
                return False

            if index == len(word) - 1:
                return True

            seen.add((i, j))

            check1 = dfs(i - 1, j, index + 1, seen) if i > 0 else False
            check2 = dfs(i + 1, j, index + 1, seen) if i < len(board) - 1 else False
            check3 = dfs(i, j - 1, index + 1, seen) if j > 0 else False
            check4 = dfs(i, j + 1, index + 1, seen) if j < len(board[i]) - 1 else False

            seen.remove((i, j))

            return check1 or check2 or check3 or check4

        for i in range(len(board)):
            for j in range(len(board[i])):
                if dfs(i, j, 0, set()):
                    return True

        return False