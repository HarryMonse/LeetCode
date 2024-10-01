from typing import List


class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sums = []
        for i in range(len(nums)-1):
            sums.append(sum(nums[i:i+2]))
        return len(sums) != len(set(sums))
            

solution_instance = Solution()

result = solution_instance.findSubarrays(nums = [4,2,4])
print(result)

result = solution_instance.findSubarrays(nums = [1,2,3,4,5])
print(result)

result = solution_instance.findSubarrays(nums = [0,0,0])
print(result)   