class Solution(object):
    def modifiedMatrix(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        for i in range(n):
            l = -1000000
            for j in range(m):
                l = matrix[j][i] if matrix[j][i] > l else l
            
            for j in range(m):
                if matrix[j][i] == -1:
                    matrix[j][i] = l

        return matrix