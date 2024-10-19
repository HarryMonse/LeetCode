class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        return goal in (s + s)
    

solution_instance = Solution()

result = solution_instance.rotateString(s = "abcde", goal = "cdeab")
print(result)

result = solution_instance.rotateString(s = "abcde", goal = "abced")
print(result)