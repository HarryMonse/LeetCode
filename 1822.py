from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for i in nums:
            product = product*i
        if product > 0:
            return 1
        elif product < 0:
            return -1
        else:
            return 0


solution_instance = Solution()

result = solution_instance.arraySign(nums = [-1,-2,-3,-4,3,2,1])
print(result)

result = solution_instance.arraySign(nums = [1,5,0,2,-3])
print(result)

result = solution_instance.arraySign(nums = [-1,1,-1,1,-1])
print(result)

        
        



        

        