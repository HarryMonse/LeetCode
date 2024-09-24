from typing import List


class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        return min(nums2) - min(nums1)
        

solution_instance = Solution()

result = solution_instance.addedInteger(nums1 = [2,6,4], nums2 = [9,7,5])
print(result)

result = solution_instance.addedInteger(nums1 = [10], nums2 = [5])
print(result)

result = solution_instance.addedInteger(nums1 = [1,1,1,1], nums2 = [1,1,1,1])
print(result)