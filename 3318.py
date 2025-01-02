from typing import Counter, List


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        i, j, ans = 0, k, []
        while j <= len(nums):
            if len(nums[i:j]) <= x:
                ans.append(sum(nums[i:j]))
            else:
                s = 0
                for n in sorted(Counter(nums[i:j]).items(), key=lambda x: (x[1], x[0]), reverse=True)[:x]:
                    s += n[0] * n[1]
                ans.append(s)
            i += 1
            j += 1
        return ans


solution_instance = Solution()

result = solution_instance.findXSum( nums = [1,1,2,2,3,4,2,3], k = 6, x = 2)
print(result)

result = solution_instance.findXSum(nums = [3,8,7,8,7,5], k = 2, x = 2)
print(result)
