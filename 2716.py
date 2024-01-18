class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))
    

solution_instance = Solution()

result = solution_instance.minimizedStringLength(s = "aaabc")
print(result)

result = solution_instance.minimizedStringLength(s = "cbbd")
print(result)

result = solution_instance.minimizedStringLength(s = "dddaaa")
print(result)
        