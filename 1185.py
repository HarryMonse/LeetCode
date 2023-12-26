from datetime import date


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return date(year, month, day).strftime("%A")
    
    
solution_instance = Solution()

result = solution_instance.dayOfTheWeek(31,8,2019)
print(result)

result = solution_instance.dayOfTheWeek(18,7,1999)
print(result)

result = solution_instance.dayOfTheWeek(15,8,1993)
print(result)