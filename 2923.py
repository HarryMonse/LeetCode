from typing import List


class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        champion = 0
    
        for i in range(1, len(grid)):
            if grid[i][champion] == 1:
                champion = i
        
        for j in range(len(grid)):
            if j != champion and grid[champion][j] == 0:
                return -1
        
        return champion
    

solution_instance = Solution()

result = solution_instance.findChampion(grid = [[0,1],[0,0]])
print(result)

result = solution_instance.findChampion(grid = [[0,0,1],[1,0,1],[0,0,0]])
print(result)