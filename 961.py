from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        list1 = []
        for i in nums :
            if i in list1 :
                return i
            else :
                list1.append(i)


solution_instance = Solution()

result = solution_instance.repeatedNTimes(nums = [1,2,3,3])
print(result)

result = solution_instance.repeatedNTimes(nums = [2,1,2,5,3,2])
print(result)

result = solution_instance.repeatedNTimes(nums = [5,1,5,2,5,3,5,4])
print(result)