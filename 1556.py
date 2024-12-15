class Solution:
    def thousandSeparator(self, n: int) -> str:
        s=str(n)
        s=s[::-1]
        res = '.'.join(s[i:i + 3] for i in range(0, len(s), 3))
        return res[::-1]


solution_instance = Solution()

result = solution_instance.thousandSeparator(n = 987)
print(result)

result = solution_instance.thousandSeparator(n = 1234)
print(result)

