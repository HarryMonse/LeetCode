from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        for i in range(n):
            if len(str(nums[i])) % 2 == 0:
                count += 1
        return count
    

solution_instance = Solution()

result = solution_instance.findNumbers(nums = [12,345,2,6,7896])
print(result)

result = solution_instance.findNumbers(nums = [555,901,482,1771])
print(result)


  