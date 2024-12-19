from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        sums = []
        for i, row in enumerate(mat):
            sums.append((sum(row), i))

        sorted_sums = sorted(sums)
        
        k_rows = sorted_sums[:k]

        res = []
        for val in k_rows:
            res.append(val[1])

        return res


solution_instance = Solution()

result = solution_instance.kWeakestRows(mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3)
print(result)

result = solution_instance.kWeakestRows(mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2)
print(result)

