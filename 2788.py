from typing import List


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        arr = []
        for i in words:
            word = i.split(separator)
            for j in word:
                if j:
                    arr.append(j)
        return arr
    

solution_instance = Solution()

result = solution_instance.splitWordsBySeparator(words = ["one.two.three","four.five","six"], separator = ".")
print(result)

result = solution_instance.splitWordsBySeparator(words = ["$easy$","$problem$"], separator = "$")
print(result)

result = solution_instance.splitWordsBySeparator(words = ["|||"], separator = "|")
print(result)