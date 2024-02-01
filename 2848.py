from typing import List


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        ans = set()
        for a, b in nums:
            for i in range(a, b+1):
                ans.add(i)
        return len(ans)


solution_instance = Solution()

result = solution_instance.numberOfPoints(nums = [[3,6],[1,5],[4,7]])
print(result)

result = solution_instance.numberOfPoints(nums = [[1,3],[5,8]])
print(result)
