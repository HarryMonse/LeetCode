class Solution:
    def maxPower(self, s: str) -> int:
        max_power = 1
        count = 1

        i = 1
        while i < len(s):
            if s[i] == s[i - 1]:
                count += 1
            else:
                count = 1
            i += 1
            max_power = max(count, max_power)

        return max_power
    

solution_instance = Solution()

result = solution_instance.maxPower(s = "leetcode")
print(result)

result = solution_instance.maxPower(s = "abbcccddddeeeeedcba")
print(result)