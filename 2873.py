from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    res = (nums[i] - nums[j]) * nums[k]
                    if res < 0:
                        res = 0
                    ans.append(res)
        return max(ans)


solution_instance = Solution()

result = solution_instance.maximumTripletValue(nums = [12,6,1,2,7])
print(result)

result = solution_instance.maximumTripletValue(nums = [1,10,3,4,19])
print(result)

result = solution_instance.maximumTripletValue(nums = [1,2,3])
print(result)
        