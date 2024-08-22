from typing import List


class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        res=[]
        for r in range(rows):
            for c in range(cols):
                res.append([r,c])           
        res.sort(key=lambda x:abs(x[0]-rCenter)+ abs(x[1]-cCenter))
        return res
    

solution_instance = Solution()

result = solution_instance.allCellsDistOrder(rows = 1, cols = 2, rCenter = 0, cCenter = 0)
print(result)

result = solution_instance.allCellsDistOrder(rows = 2, cols = 2, rCenter = 0, cCenter = 1)
print(result)

result = solution_instance.allCellsDistOrder(rows = 2, cols = 3, rCenter = 1, cCenter = 2)
print(result)