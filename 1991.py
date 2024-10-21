from typing import List


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        sum1 = 0
        for i in range(len(nums)):
            sum2 = total_sum - sum1 - nums[i]
            if sum1 == sum2:
                return i
            sum1 += nums[i]
        return -1


solution_instance = Solution()

result = solution_instance.findMiddleIndex(nums = [2,3,-1,8,4])
print(result)

result = solution_instance.findMiddleIndex(nums = [1,-1,4])
print(result)

result = solution_instance.findMiddleIndex(nums = [2,5])
print(result)