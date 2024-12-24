from typing import List


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        ans = 0
        count = 0
        for i in rectangles:
            temp = min(i)
            if temp > ans:
                ans = temp
                count = 1
            elif temp == ans:
                count += 1
        return count


solution_instance = Solution()

result = solution_instance.countGoodRectangles(rectangles = [[5,8],[3,9],[5,12],[16,5]])
print(result)

result = solution_instance.countGoodRectangles(rectangles = [[2,3],[3,7],[4,3],[3,7]])
print(result)