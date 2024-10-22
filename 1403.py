from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        ans=[]
        nums.sort()
        while sum(nums)>sum(ans):
            ans.append(nums.pop())
        if sum(nums)==sum(ans):
            ans.append(nums.pop())
        return ans
    

solution_instance = Solution()

result = solution_instance.minSubsequence(nums = [4,3,10,9,8])
print(result)

result = solution_instance.minSubsequence(nums = [4,4,7,6,7])
print(result)

