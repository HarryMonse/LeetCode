class Solution:
    def countPoints(self, rings: str) -> int:
        ans = 0
        for i in range(10):
            i = str(i)
            if 'R'+i in rings and 'G'+i in rings and 'B'+i in rings:
                ans += 1
        return ans
    

solution_instance = Solution()

result = solution_instance.countPoints(rings = "B0B6G0R6R0R6G9")
print(result)

result = solution_instance.countPoints(rings = "B0R0G0R9R0B0G0")
print(result)

result = solution_instance.countPoints(rings = "G4")
print(result)