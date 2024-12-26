from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        generated = []  
        for i in range(0, len(nums), 2):  
            freq = nums[i]
            val = nums[i+1]  
            generated += [val] * freq  
        return generated


solution_instance = Solution()

result = solution_instance.decompressRLElist(nums = [1,2,3,4])
print(result)

result = solution_instance.decompressRLElist(nums = [1,1,2,3])
print(result)

