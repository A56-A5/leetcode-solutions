class Solution {
    public int[][] modifiedMatrix(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        
        for (int col = 0; col < n; col++) {
            int maxInCol = Integer.MIN_VALUE;
            for (int row = 0; row < m; row++) {
                if (matrix[row][col] != -1 && matrix[row][col] > maxInCol) {
                    maxInCol = matrix[row][col];
                }
            }
            for (int row = 0; row < m; row++) {
                if (matrix[row][col] == -1) {
                    matrix[row][col] = maxInCol;
                }
            }
        }
        
        return matrix;
    }
}