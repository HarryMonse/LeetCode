from typing import List


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0
        for i in hours:
            if i >= target:
                count += 1
        return count


solution_instance = Solution()

result = solution_instance.numberOfEmployeesWhoMetTarget(hours = [0,1,2,3,4], target = 2)
print(result)

result = solution_instance.numberOfEmployeesWhoMetTarget(hours = [5,1,4,2,2], target = 6)
print(result)

        