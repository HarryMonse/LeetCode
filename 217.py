from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
    

solution_instance = Solution()

result = solution_instance.containsDuplicate(nums = [1,2,3,1])
print(result)

result = solution_instance.containsDuplicate(nums = [1,2,3,4])
print(result)

result = solution_instance.containsDuplicate(nums = [1,1,1,3,3,4,3,2,4,2])
print(result)

        