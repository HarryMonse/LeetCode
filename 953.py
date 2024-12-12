from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        h = {ch: i for i, ch in enumerate(order)}
        prev = list(h[ch] for ch in words[0])
        for i in range(1, len(words)):
            cur = list(h[ch] for ch in words[i])
            if cur < prev:
                return False
            prev = cur
        return True


solution_instance = Solution()

result = solution_instance.isAlienSorted(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz")
print(result)

result = solution_instance.isAlienSorted(words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz")
print(result)

result = solution_instance.isAlienSorted(words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz")
print(result)