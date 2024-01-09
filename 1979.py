from math import gcd
from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return gcd(min(nums),max(nums))
    

solution_instance = Solution()

result = solution_instance.findGCD(nums = [2,5,6,9,10])
print(result)

result = solution_instance.findGCD(nums = [7,5,6,8,3])
print(result)

result = solution_instance.findGCD(nums = [3,3])
print(result)


        