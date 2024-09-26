from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            if nums.count(i) > 1:
                ans.append(i)
        return list(set(ans))
    

solution_instance = Solution()

result = solution_instance.getSneakyNumbers(nums = [0,1,1,0])
print(result)

result = solution_instance.getSneakyNumbers(nums = [0,3,2,1,3,2])
print(result)

result = solution_instance.getSneakyNumbers(nums = [7,1,5,4,3,4,6,0,9,5,8,2])
print(result)
