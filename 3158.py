from typing import List


class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        countMap = {}
        for num in nums:
            countMap[num] = countMap.get(num, 0) + 1
        result = 0
        for num, count in countMap.items():
            if count == 2:
                result ^= num
        return result


solution_instance = Solution()

result = solution_instance.duplicateNumbersXOR(nums = [1,2,1,3])
print(result)

result = solution_instance.duplicateNumbersXOR(nums = [1,2,3])
print(result)

result = solution_instance.duplicateNumbersXOR(nums = [1,2,2,1])
print(result)