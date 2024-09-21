from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        ans = []
        for i in points:
            ans.append(i[0])
        ans = sorted(ans)
        diff = 0 
        for i in range(len(ans)-1):
            new = abs(ans[i] - ans[i+1])
            if new > diff:
                diff = new
        return diff


solution_instance = Solution()

result = solution_instance.maxWidthOfVerticalArea(points = [[8,7],[9,9],[7,4],[9,7]])
print(result)

result = solution_instance.maxWidthOfVerticalArea(points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]])
print(result)     