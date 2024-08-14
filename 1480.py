from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = []
        for i in range(len(nums)):
            newSum = sum(nums[:i+1])
            runningSum.append(newSum)
        return runningSum
        

solution_instance = Solution()

result = solution_instance.runningSum(nums = [1,2,3,4])
print(result)

result = solution_instance.runningSum(nums = [1,1,1,1,1])
print(result)

result = solution_instance.runningSum(nums = [3,1,2,10,1])
print(result)