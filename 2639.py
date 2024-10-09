from typing import List


class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        columns = [[] for i in range(n)]
        ans = []
        cn = 0
        for col in grid:
            for j in range(len(col)):
                columns[j].append(len(str(col[j])))
        for column in columns:
            ans.append(max(column))   
        return ans


solution_instance = Solution()

result = solution_instance.findColumnWidth(grid = [[1],[22],[333]])
print(result)

result = solution_instance.findColumnWidth(grid = [[-15,1,3],[15,7,12],[5,6,-2]])
print(result)