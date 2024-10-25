from itertools import accumulate
from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        return max(1, 1 - min(accumulate(nums)))
    

solution_instance = Solution()

result = solution_instance.minStartValue(nums = [-3,2,-3,4,2])
print(result)

result = solution_instance.minStartValue(nums = [1,2])
print(result)

result = solution_instance.minStartValue(nums = [1,-2,-3])
print(result)