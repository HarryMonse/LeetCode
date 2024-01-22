from typing import List


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        sum = 0
        n = len(nums)
        for i in range(n):
            if n % (i+1) == 0:
                sum += nums[i] ** 2
        return sum
    

solution_instance = Solution()

result = solution_instance.sumOfSquares(nums = [1,2,3,4])
print(result)

result = solution_instance.sumOfSquares(nums = [2,7,1,19,18,3])
print(result)
        