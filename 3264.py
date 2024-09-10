from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            minimum=min(nums)
            index=nums.index(minimum)
            value=minimum*multiplier
            nums[index]=value
        return nums
    

solution_instance = Solution()

result = solution_instance.getFinalState(nums = [2,1,3,5,6], k = 5, multiplier = 2)
print(result)

result = solution_instance.getFinalState(nums = [1,2], k = 3, multiplier = 4)
print(result)
