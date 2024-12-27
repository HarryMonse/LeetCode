from typing import List


class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        m = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                    m = max(m, nums[i] ^ nums[j])
        return m


solution_instance = Solution()

result = solution_instance.maximumStrongPairXor(nums = [1,2,3,4,5])
print(result)

result = solution_instance.maximumStrongPairXor(nums = [10,100])
print(result)

result = solution_instance.maximumStrongPairXor(nums = [5,6,25,30])
print(result)