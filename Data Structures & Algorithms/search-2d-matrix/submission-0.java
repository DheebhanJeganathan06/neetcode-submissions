class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int l = 0, r = matrix.length * matrix[0].length - 1;

        while(l <= r && l >= 0 && r <= matrix.length * matrix[0].length - 1) {
            int i = (l + r) / 2;
            int row = i / matrix[0].length;
            int col = i % matrix[0].length;

            if(matrix[row][col] == target) {
                return true;
            }
            else if (matrix[row][col] < target) {
                l = i + 1;
            }
            else {
                r = i - 1;
            }
        }

        return false;
    }
}