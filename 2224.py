class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        ans = 0
        h, m = list(map(int, current.split(':')))
        newH, newM = list(map(int, correct.split(':')))
        d = 60*(newH - h) + newM - m
        for x in [60, 15, 5, 1]:
            ans += d//x
            d %= x
        return ans 


solution_instance = Solution()

result = solution_instance.convertTime(current = "02:30", correct = "04:35")
print(result)

result = solution_instance.convertTime(current = "11:00", correct = "11:01")
print(result)