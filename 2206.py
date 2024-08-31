from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        for i in nums:
            if nums.count(i) % 2 == 1:
                return False
        return True
                
        
solution_instance = Solution()

result = solution_instance.divideArray(nums = [3,2,3,2,2,2])
print(result)

result = solution_instance.divideArray(nums = [1,2,3,4])
print(result)