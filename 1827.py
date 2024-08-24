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