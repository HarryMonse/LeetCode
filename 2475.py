from typing import List

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:

        c = 0 

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]!=nums[j] and nums[i]!=nums[k] and nums[j]!=nums[k]:
                        c +=1 

        return c
    

solution_instance = Solution()

nums1 = [4, 4, 2, 4, 3]
result1 = solution_instance.unequalTriplets(nums1)
print(f'Test Case 1: {result1}')

nums2 = [1, 1, 1, 1, 1]
result2 = solution_instance.unequalTriplets(nums2)
print(f'Test Case 2: {result2}')






