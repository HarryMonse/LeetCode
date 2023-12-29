from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        if len(nums) > 2:
            return nums[-3]
        return nums[-1]
    
    
solution_instance = Solution()

result = solution_instance.thirdMax([3,2,1])
print(result)

result = solution_instance.thirdMax([1,2])
print(result)

result = solution_instance.thirdMax([2,2,3,1])
print(result)
       