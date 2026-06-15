class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        rowL, rowR = 0, len(matrix) - 1

        while rowL <= rowR:
            rowM = rowL + ((rowR - rowL) // 2)
            if target >= matrix[rowM][0] and target <= matrix[rowM][-1]:
                break
            elif target < matrix[rowM][0]:
                rowR = rowM - 1
            else:
                rowL = rowM + 1
        
        colL, colR = 0, len(matrix[rowM]) - 1

        while colL <= colR:
            colM = colL + ((colR - colL) // 2)
            if target == matrix[rowM][colM]:
                return True
            elif target < matrix[rowM][colM]:
                colR = colM - 1
            else:
                colL = colM + 1
                
        return False

