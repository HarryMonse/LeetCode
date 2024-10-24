from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ind_j = []
        for ind, elem in enumerate(nums):
            if elem == key:
                ind_j.append(ind)
        res = []
        for i in range(len(nums)):
            for j in ind_j:
                if abs(i - j) <= k:
                    res.append(i)
                    break
        return sorted(res)


solution_instance = Solution()

result = solution_instance.findKDistantIndices(nums = [3,4,9,1,3,9,5], key = 9, k = 1)
print(result)

result = solution_instance.findKDistantIndices(nums = [2,2,2,2,2], key = 2, k = 2)
print(result)