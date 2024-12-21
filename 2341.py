from typing import List


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        pair = 0
        count = 0
        nums_set = set(nums)
        for i in nums_set:
            temp = nums.count(i)
            pair += temp // 2
            count += temp % 2
        return [pair, count]
    

solution_instance = Solution()

result = solution_instance.numberOfPairs(nums = [1,3,2,1,3,2,2])
print(result)

result = solution_instance.numberOfPairs(nums = [1,1])
print(result)

result = solution_instance.numberOfPairs(nums = [0])
print(result)
