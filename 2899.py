from typing import List


class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen = []
        ans = []
        k = 0
        for i in range(len(nums)):
            if nums[i] > -1 :
                seen.insert(0, nums[i])
            else:
                if k < len(seen) and nums[i - 1] == -1:
                    k += 1
                    ans.append(seen[k - 1])
                elif k < len(seen):
                    k = 1
                    ans.append(seen[0])
                else:
                    ans.append(-1)
        return ans
    

solution_instance = Solution()

result = solution_instance.lastVisitedIntegers(nums = [1,2,-1,-1,-1])
print(result)

result = solution_instance.lastVisitedIntegers(nums = [1,-1,2,-1,-1])
print(result)