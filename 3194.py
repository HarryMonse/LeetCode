from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        return min((nums[i] + nums[~i]) / 2 for i in range(len(nums) >> 1))
    

solution_instance = Solution()

result = solution_instance.minimumAverage(nums = [7,8,3,4,15,13,4,1])
print(result)

result = solution_instance.minimumAverage(nums = [1,9,8,3,10,5])
print(result)

result = solution_instance.minimumAverage(nums = [1,2,3,7,8,9])
print(result)