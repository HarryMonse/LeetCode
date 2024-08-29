from collections import Counter
from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return Counter(target) == Counter(arr)
    

solution_instance = Solution()

result = solution_instance.canBeEqual(target = [1,2,3,4], arr = [2,4,1,3])
print(result)

result = solution_instance.canBeEqual(target = [7], arr = [7])
print(result)

result = solution_instance.canBeEqual(target = [3,7,9], arr = [3,7,11])
print(result)