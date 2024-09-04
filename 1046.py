from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort(reverse = True)
            first = stones.pop(0)
            second = stones.pop(0)
            if first != second:
                stones.append(first-second)
        return stones[0] if stones else 0
    

solution_instance = Solution()

result = solution_instance.lastStoneWeight(stones = [2,7,4,1,8,1])
print(result)

result = solution_instance.lastStoneWeight(stones = [1])
print(result)