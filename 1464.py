from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1]-1) * (nums[-2]-1)


solution_instance = Solution()

result = solution_instance.maxProduct(nums = [3,4,5,2])
print(result)

result = solution_instance.maxProduct(nums = [1,5,4,5])
print(result)

result = solution_instance.maxProduct(nums = [3,7])
print(result)