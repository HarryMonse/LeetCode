class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return {s1[0], s1[2]} == {s2[0], s2[2]} and {s1[1], s1[3]} == {s2[1], s2[3]}


solution_instance = Solution()

result = solution_instance.canBeEqual(s1 = "abcd", s2 = "cdab")
print(result)

result = solution_instance.canBeEqual(s1 = "abcd", s2 = "dacb")
print(result)
