from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[: : 2])
    

solution_instance = Solution()

result = solution_instance.arrayPairSum(nums = [1,4,3,2])
print(result)

result = solution_instance.arrayPairSum(nums = [6,2,6,5,1,2])
print(result)