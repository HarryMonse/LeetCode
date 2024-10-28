from typing import List


class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left=0
        right=n-1
        ans=[]
        while left<n:
            ans.append(len(set(nums[0:left+1]))-len(set(nums[left+1:right+1])))
            right+=1
            left+=1
        return ans    


solution_instance = Solution()

result = solution_instance.distinctDifferenceArray(nums = [1,2,3,4,5])
print(result)

result = solution_instance.distinctDifferenceArray(nums = [3,2,3,4,2])
print(result)