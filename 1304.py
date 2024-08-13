from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        for i in range(1, n//2 + 1):
            res.append(i)
            res.append(-i)
        if n % 2 != 0:
            res.append(0)
        return res
    

solution_instance = Solution()

result = solution_instance.sumZero(n = 5)
print(result)

result = solution_instance.sumZero(n = 3)
print(result)

result = solution_instance.sumZero(n = 1)
print(result)