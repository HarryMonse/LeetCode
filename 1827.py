from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)-1):
            if nums[i]>=nums[i+1]:
                ans=ans+nums[i]-nums[i+1]+1
                nums[i+1]=nums[i]+1
            else:
                ans+=0
        return ans
    

solution_instance = Solution()

result = solution_instance.minOperations(nums = [1,1,1])
print(result)

result = solution_instance.minOperations(nums = [1,5,2,4,1])
print(result)

result = solution_instance.minOperations(nums = [8])
print(result)