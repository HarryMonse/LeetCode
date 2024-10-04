from typing import List


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        ans = 0
        for i in range(len(hours)):
            for j in range(i + 1, len(hours)):
                if (hours[i] + hours[j]) % 24 == 0 :
                    ans += 1
        return ans


solution_instance = Solution()

result = solution_instance.countCompleteDayPairs(hours = [12,12,30,24,24])
print(result)

result = solution_instance.countCompleteDayPairs(hours = [72,48,24,3])
print(result)
