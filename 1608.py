from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for x in range(1, len(nums) + 1):
            if nums[x-1] >= x and (x == len(nums) or nums[x] < x):
                return x
        return -1


solution_instance = Solution()

result = solution_instance.specialArray(nums = [3,5])
print(result)

result = solution_instance.specialArray(nums = [0,0])
print(result)

result = solution_instance.specialArray(nums = [0,4,3,0,4])
print(result)

