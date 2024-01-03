from typing import List


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = [] 
        for i in nums:
            for j in str(i):
                res.append(int(j))
        return res
    

solution_instance = Solution()

result = solution_instance.separateDigits(nums = [13,25,83,77])
print(result)

result = solution_instance.separateDigits(nums = [7,1,3,9])
print(result)

        
        