from typing import Counter, List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        i = len(words)-1
        while i > 0:
            if Counter(words[i]) == Counter(words[i-1]):
                words.pop(i)
            i -= 1
        return words


solution_instance = Solution()

result = solution_instance.removeAnagrams(words = ["abba","baba","bbaa","cd","cd"])
print(result)

result = solution_instance.removeAnagrams(words = ["a","b","c","d","e"])
print(result)

