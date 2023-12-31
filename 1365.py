from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = 0 
        new_list = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j and nums[j] < nums[i]:
                    count += 1
            new_list.append(count)
            count = 0 
        return new_list
    

solution_instance = Solution()

result = solution_instance.smallerNumbersThanCurrent([8,1,2,2,3])
print(result)

result = solution_instance.smallerNumbersThanCurrent([6,5,4,8])
print(result)

result = solution_instance.smallerNumbersThanCurrent([7,7,7,7])
print(result)



        