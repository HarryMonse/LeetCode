from typing import List


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        a=[]
        for i in range(len(nums)//2):
            a.append((max(nums)+min(nums))/2)
            nums.remove(max(nums))
            nums.remove(min(nums))
            b=set(a)

        return len(b)


solution_instance = Solution()

result = solution_instance.distinctAverages(nums = [4,1,4,0,3,5])
print(result)

result = solution_instance.distinctAverages(nums = [1,100])
print(result)