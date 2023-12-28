from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([x**2 for x in nums])
    
solution_instance = Solution()

result = solution_instance.sortedSquares([-4,-1,0,3,10])
print(result)

result = solution_instance.sortedSquares([-7,-3,2,3,11])
print(result)


        