from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = {}
        sorted_arr = sorted(list(set(arr)))
        for i in range(len(sorted_arr)):
            ranks[sorted_arr[i]] = i + 1
        for i in range(len(arr)):
            arr[i] = ranks[arr[i]]
        return arr
    

solution_instance = Solution()

result = solution_instance.arrayRankTransform(arr = [40,10,20,30])
print(result)

result = solution_instance.arrayRankTransform(arr = [100,100,100])
print(result)

result = solution_instance.arrayRankTransform(arr = [37,12,28,9,100,56,80,5,12])
print(result)
        