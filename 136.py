from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        my_dict = {}

        for i in range(len(nums)):
            if nums[i] not in my_dict:
                my_dict[nums[i]] = 1
            else:
                my_dict.pop(nums[i])

        return int(*my_dict)
                
        
solution_instance = Solution()

result = solution_instance.singleNumber([2,2,1])
print(result)

result = solution_instance.singleNumber([4,1,2,1,2])
print(result)

result = solution_instance.singleNumber([1])
print(result)

