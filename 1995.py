from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        count = 0
        for a in range(len(nums)):
            for b in range(a+1, len(nums)):
                for c in range(b+1, len(nums)):
                    for d in range(c+1, len(nums)):
                        if nums[a] + nums[b] + nums[c] == nums[d]:
                            count += 1
        return count


solution_instance = Solution()

result = solution_instance.countQuadruplets(nums = [1,2,3,6])
print(result)

result = solution_instance.countQuadruplets(nums = [3,3,6,4,5])
print(result)

result = solution_instance.countQuadruplets(nums = [1,1,1,3,5])
print(result)