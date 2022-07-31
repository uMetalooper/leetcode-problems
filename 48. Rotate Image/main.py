from typing import List


mprint = lambda A: print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in A]))


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # transpose
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # left-to-right flip
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]

matrix = [[1,2,3],[4,5,6],[7,8,9]]
mprint(matrix)
print("----------------------------")
Solution().rotate(matrix)
mprint(matrix)