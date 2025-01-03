from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0                
        temp = []
        zeros = []
        a=nums
        for i in range(len(a)):
            if a[i] !=0:
                temp.append(a[i])
            else:
                zeros.append(a[i])
        return (temp+zeros)


solution_instance = Solution()

result = solution_instance.applyOperations(nums = [1,2,2,1,1,0])
print(result)

result = solution_instance.applyOperations(nums = [0,1])
print(result)