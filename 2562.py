from typing import List


class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        ans = 0
        while nums:
            p = str(nums.pop(0))
            q = ""
            if nums:
                q = str(nums.pop())
            ans += int(p+q)
        return ans


solution_instance = Solution()

result = solution_instance.findTheArrayConcVal(nums = [7,52,2,4])
print(result)

result = solution_instance.findTheArrayConcVal(nums = [5,14,13,8,12])
print(result)
        