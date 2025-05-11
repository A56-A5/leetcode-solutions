class Solution {
    public int[] rowAndMaximumOnes(int[][] mat) {
        int row = 0, c = 0;

        for (int i = 0; i < mat.length; i++) {
            int ones = 0;
            for (int j = 0; j < mat[i].length; j++) {
                if (mat[i][j] == 1) {
                    ones++;
                }
            }
            if (ones > c) {
                c = ones;
                row = i;
            }
        }
        return new int[]{row, c};
    }
}
