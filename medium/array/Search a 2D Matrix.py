class Solution(object):
    def searchMatrix(self, matrix, target):
        for row in matrix:
            for i in row:
                if target == i:
                    return True
        return False
        