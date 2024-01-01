from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        result = 0
        for i in nums:
            if nums.count(i) == 1:
                result += i
        return result


solution_instance = Solution()

result = solution_instance.sumOfUnique([1,2,3,2])
print(result)

result = solution_instance.sumOfUnique([1,1,1,1,1])
print(result)

result = solution_instance.sumOfUnique([1,2,3,4,5])
print(result)
        