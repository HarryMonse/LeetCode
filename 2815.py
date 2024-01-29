from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        temp = 0 
        l = len(nums)
        for i in range(l-1):
            nums1 = max(str(nums[i]))
            for j in range(i+1,l):
                nums2 = max(str(nums[j]))
                if nums1 == nums2:
                    temp = max(temp, nums[i] + nums[j])
        return -1 if temp == 0 else temp
    

solution_instance = Solution()

result = solution_instance.maxSum([51,71,17,24,42])
print(result)

result = solution_instance.maxSum([1,2,3,4])
print(result)


        