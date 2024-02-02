from typing import List


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ans = 0 
        for index, num in enumerate(nums):
            binary_index = str(bin(index))
            if binary_index.count("1") == k:
                ans += num
        return ans


solution_instance = Solution()

result = solution_instance.sumIndicesWithKSetBits(nums = [5,10,1,5,2], k = 1)
print(result)

result = solution_instance.sumIndicesWithKSetBits(nums = [4,3,2,1], k = 2)
print(result)
    