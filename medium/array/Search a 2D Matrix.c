bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target) {
    for(int i=0;i<matrixSize;i++){
        for(int k=0;k<matrixSize;k++){
            for(int j=0;j<matrixColSize[k];j++){
                if(matrix[i][j]==target) return true;
            }
        }
    }return false;
}