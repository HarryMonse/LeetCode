from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_so_far = max_overall = nums[0]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                max_so_far += nums[i]
                max_overall = max(max_overall, max_so_far)
            else: 
                max_so_far = nums[i]
        return max_overall   


solution_instance = Solution()

result = solution_instance.maxAscendingSum(nums = [10,20,30,5,10,50])
print(result)

result = solution_instance.maxAscendingSum(nums = [10,20,30,40,50])
print(result)

result = solution_instance.maxAscendingSum(nums = [12,17,15,13,10,11,12])
print(result)