from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        nums.sort()
        min_diff = max(nums)
        for i in range(len(nums)-k+1):
            diff = abs(nums[i]- nums[i+k-1])
            min_diff = min(min_diff, diff)
        return min_diff
    

solution_instance = Solution()

result = solution_instance.minimumDifference(nums = [90], k = 1)
print(result)

result = solution_instance.minimumDifference(nums = [9,4,1,7], k = 2)
print(result)

