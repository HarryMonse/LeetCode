from typing import Counter, List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq_map = Counter(nums)
        nums.sort(key=lambda x: (freq_map[x], -x))
        return nums
    

solution_instance = Solution()

result = solution_instance.frequencySort(nums = [1,1,2,2,2,3])
print(result)

result = solution_instance.frequencySort(nums = [2,3,1,3,2])
print(result)

result = solution_instance.frequencySort([-1,1,-6,4,5,-6,1,4,1])
print(result)