from collections import defaultdict
from typing import List


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        a, c, b =  defaultdict(int), [], items1 + items2
        for j in b:
            if j[0] not in a:  a[j[0]] = j[1]
            else: a[j[0]] = a[j[0]] + j[1]
        for i in sorted(a): c.append([i,a[i]])
        return c
    

solution_instance = Solution()

result = solution_instance.mergeSimilarItems(items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5]])
print(result)

result = solution_instance.mergeSimilarItems(items1 = [[1,1],[3,2],[2,3]], items2 = [[2,1],[3,2],[1,3]])
print(result)

result = solution_instance.mergeSimilarItems(items1 = [[1,3],[2,2]], items2 = [[7,1],[2,2],[1,4]])
print(result)
