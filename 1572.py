from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        s = 0
        for i in range(n):
            s += mat[i][i]
            if n-i-1 != i:
                s += mat[i][n-i-1]
        return s


solution_instance = Solution()

result = solution_instance.diagonalSum(mat = [[1,2,3],
              [4,5,6],
              [7,8,9]])
print(result)

result = solution_instance.diagonalSum(mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]])
print(result)

result = solution_instance.diagonalSum(mat = [[5]])
print(result)