class Solution(object):
    def rowAndMaximumOnes(self, mat):
        row,c=0,0
        for i in range(len(mat)):
            one=0
            for j in range(len(mat[0])):
                if mat[i][j]==1:
                    one+=1
            if one>c:
                c=one
                row=i

        return [row,c]
