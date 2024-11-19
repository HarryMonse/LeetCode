from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            for j in range(i):
                if j | (j + 1) == i:
                    ans.append(j)
                    break
            else:
                ans.append(-1)
        return ans


solution_instance = Solution()

result = solution_instance.minBitwiseArray(nums = [2,3,5,7])
print(result)

result = solution_instance.minBitwiseArray(nums = [11,13,31])
print(result)

