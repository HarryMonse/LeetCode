from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while original in nums:
            original*=2
        return original
    

solution_instance = Solution()

result = solution_instance.findFinalValue(nums = [5,3,6,1,12], original = 3)
print(result)

result = solution_instance.findFinalValue(nums = [2,7,9], original = 4)
print(result)
