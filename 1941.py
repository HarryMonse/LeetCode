class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        ans = s.count(s[0])
        for i in s:
            if s.count(i) != ans:
                return False
        return True


solution_instance = Solution()

result = solution_instance.areOccurrencesEqual(s = "abacbc")
print(result)

result = solution_instance.areOccurrencesEqual(s = "aaabb")
print(result)
