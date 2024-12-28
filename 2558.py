import math
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts.sort()
        n = len(gifts)

        for _ in range(k):
            gifts[-1] = int(math.sqrt(gifts[-1]))
            gifts.sort()

        return sum(gifts)
    

solution_instance = Solution()

result = solution_instance.pickGifts(gifts = [25,64,9,4,100], k = 4)
print(result)

result = solution_instance.pickGifts(gifts = [1,1,1,1], k = 4)
print(result)