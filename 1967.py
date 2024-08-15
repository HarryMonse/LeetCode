from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for i in patterns:
            if i in word:
                count += 1
        return count
    

solution_instance = Solution()

result = solution_instance.numOfStrings(patterns = ["a","abc","bc","d"], word = "abc")
print(result)

result = solution_instance.numOfStrings(patterns = ["a","b","c"], word = "aaaaabbbbb")
print(result)

result = solution_instance.numOfStrings(patterns = ["a","a","a"], word = "ab")
print(result)

        