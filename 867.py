from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res[j][i]=matrix[i][j]
        return res


solution_instance = Solution()

result = solution_instance.transpose(matrix = [[1,2,3],[4,5,6],[7,8,9]])
print(result)

result = solution_instance.transpose(matrix = [[1,2,3],[4,5,6]])
print(result)

