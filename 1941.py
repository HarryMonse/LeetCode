class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        ans = s.count(s[0])
        for i in s:
            if s.count(i) != ans:
                return False
        return True
        