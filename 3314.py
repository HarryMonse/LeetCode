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

result = solution_instance.minBitwiseArray(nums = [0,1,1,0])
print(result)

result = solution_instance.minBitwiseArray(nums = [0,3,2,1,3,2])
print(result)

