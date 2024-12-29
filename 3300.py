from typing import List


class Solution:
    def minElement(self, nums: List[int]) -> int:
        mini=float('inf')
        for num in nums:
            r=0
            while num>0:
                r+= num%10
                num//=10
            mini= min(mini, r)
        return mini


solution_instance = Solution()

result = solution_instance.minElement(nums = [10,12,13,14])
print(result)

result = solution_instance.minElement(nums = [1,2,3,4])
print(result)

result = solution_instance.minElement(nums = [999,19,199])
print(result)

