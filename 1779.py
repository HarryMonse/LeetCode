from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        valid=[]
        for i in points:
            if i[0]==x or i[1]==y:
                valid.append(i)
        dist=[]
        if len(valid) == 0:
            return -1
        else :
            for i in valid:
                dist.append(abs(x - i[0]) + abs(y - i[1]))
            if valid[dist.index(min(dist))] in valid:
                return points.index(valid[dist.index(min(dist))])
            
solution_instance = Solution()

result = solution_instance.nearestValidPoint(x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]])
print(result)

result = solution_instance.nearestValidPoint(x = 3, y = 4, points = [[3,4]])
print(result)

result = solution_instance.nearestValidPoint(x = 3, y = 4, points = [[2,3]])
print(result)