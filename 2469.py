from typing import List


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius * 1.80 + 32.00]
    

solution_instance = Solution()

result = solution_instance.convertTemperature(celsius = 36.50)
print(result)

result = solution_instance.convertTemperature(celsius = 122.11)
print(result)
        