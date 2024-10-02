from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for i in range(len(words)):
            for j in range(len(words)):
                if words[i] in words[j] and i != j:
                    ans.append(words[i])
                    break
        return ans


solution_instance = Solution()

result = solution_instance.stringMatching(words = ["mass","as","hero","superhero"])
print(result)

result = solution_instance.stringMatching(words = ["leetcode","et","code"])
print(result)

result = solution_instance.stringMatching(words = ["blue","green","bu"])
print(result)
        