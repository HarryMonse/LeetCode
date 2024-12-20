from typing import List


class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(32):
            count = 0
            n = 2**i
            for num in nums:
                if num & n:
                    count += 1
            if count >= k:
                res += n
        return res
    

solution_instance = Solution()

result = solution_instance.findKOr(nums = [7,12,9,8,9,15], k = 4)
print(result)

result = solution_instance.findKOr(nums = [2,12,1,11,4,5], k = 6)
print(result)

result = solution_instance.findKOr(nums = [10,8,5,9,11,6,8], k = 1)
print(result)

