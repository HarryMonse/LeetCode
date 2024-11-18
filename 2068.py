class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        words = set(word1 + word2)
        for w in words:
            if abs(word1.count(w) - word2.count(w)) >3:
                return False
        return True


solution_instance = Solution()

result = solution_instance.checkAlmostEquivalent(word1 = "aaaa", word2 = "bccb")
print(result)

result = solution_instance.checkAlmostEquivalent(word1 = "abcdeef", word2 = "abaaacc")
print(result)

result = solution_instance.checkAlmostEquivalent(word1 = "cccddabba", word2 = "babababab")
print(result)

