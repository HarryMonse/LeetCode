from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr=[first]
        for num in encoded: arr.append(arr[-1]^num)
        return arr
    

solution_instance = Solution()

result = solution_instance.decode(encoded = [1,2,3], first = 1)
print(result)

result = solution_instance.decode(encoded = [6,2,7,3], first = 4)
print(result)

