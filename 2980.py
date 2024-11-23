from typing import List


class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        l = []
        count = 0
        for i in range(len(nums)):
            if nums[i]%2==0:
                count+=1
            if count>1:
                return True
        return False


solution_instance = Solution()

result = solution_instance.hasTrailingZeros(nums = [1,2,3,4,5])
print(result)

result = solution_instance.hasTrailingZeros(nums = [2,4,8,16])
print(result)

result = solution_instance.hasTrailingZeros(nums = [1,3,5,7,9])
print(result)