from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mappedNums = {}
        for num in nums:
            if num in mappedNums: continue
            mappedNums[num] = int(''.join(str(mapping[int(d)]) for d in str(num)))

        return sorted(nums, key = mappedNums.get)
    

solution_instance = Solution()

result = solution_instance.sortJumbled(mapping = [8,9,4,0,2,1,3,5,7,6], nums = [991,338,38])
print(result)

result = solution_instance.sortJumbled(mapping = [0,1,2,3,4,5,6,7,8,9], nums = [789,456,123])
print(result)

