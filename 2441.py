from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        
        nums.sort()
        for i in nums[::-1]:
            if -i in nums:
                return i 

        return -1
    

solution_instance = Solution()

nums1 = [-1, 2 ,-3, 3]
result1 = solution_instance.findMaxK(nums1)
print(f'Test Case 1: {result1}') 

nums2 = [-1, 10, 6, 7, -7, 1]
result2 = solution_instance.findMaxK(nums2)
print(f'Test Case 2: {result2}')

nums3 = [-10, 8, 6, 7, -2, -3]
result3 = solution_instance.findMaxK(nums3)
print(f'Test Case 3: {result3}')





        
        