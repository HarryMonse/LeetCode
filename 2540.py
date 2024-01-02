from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        st = set(nums1) & set(nums2)
        return min(st) if len(st) else -1


solution_instance = Solution()

result = solution_instance.getCommon(nums1 = [1,2,3], nums2 = [2,4])
print(result)

result = solution_instance.getCommon(nums1 = [1,2,3,6], nums2 = [2,3,4,5])
print(result)

        