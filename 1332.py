class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 1 if s == s[::-1] else 2
    

solution_instance = Solution()

result = solution_instance.removePalindromeSub(s = "ababa")
print(result)

result = solution_instance.removePalindromeSub(s = "abb")
print(result)

result = solution_instance.removePalindromeSub(s = "baabb")
print(result)