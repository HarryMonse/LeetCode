from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        sec = set(path[1] for path in paths)
        fir = set(path[0] for path in paths)
        ans = sec - fir
        return ans.pop()


solution_instance = Solution()

result = solution_instance.destCity(paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]])
print(result)

result = solution_instance.destCity(paths = [["B","C"],["D","B"],["C","A"]])
print(result)

result = solution_instance.destCity(paths = [["A","Z"]])
print(result)