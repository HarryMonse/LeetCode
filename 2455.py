from typing import List


class Solution:
    def averageValue(self, nums: List[int]) -> int:
        res = [i for i in nums if i % 2 == 0 and i % 3 == 0]
        return sum(res)//len(res) if len(res) > 0 else 0
                

solution_instance = Solution()

result = solution_instance.averageValue(nums = [1,3,6,10,12,15])
print(result)

result = solution_instance.averageValue(nums = [1,2,4,7,10])
print(result)