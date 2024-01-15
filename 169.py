from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]


solution_instance = Solution()

result = solution_instance.majorityElement(nums = [3,2,3])
print(result)

result = solution_instance.majorityElement(nums = [2,2,1,1,1,2,2])
print(result)


        