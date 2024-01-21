from typing import List


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        common = set(nums1).intersection(nums2)
        m1 = min(nums1)
        m2 = min(nums2)
        return min(common) if common else min(m1, m2) * 10 + max(m1, m2)
    

solution_instance = Solution()

result = solution_instance.minNumber(nums1 = [4,1,3], nums2 = [5,7])
print(result)

result = solution_instance.minNumber(nums1 = [3,5,2,6], nums2 = [3,1,7])
print(result)

        