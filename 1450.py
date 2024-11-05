from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        res = 0
        for i in range(len(startTime)):
            if queryTime >= startTime[i] and endTime[i] >= queryTime :
                res += 1
        return res
    

solution_instance = Solution()

result = solution_instance.busyStudent(startTime = [1,2,3], endTime = [3,2,7], queryTime = 4)
print(result)

result = solution_instance.busyStudent(startTime = [4], endTime = [4], queryTime = 4)
print(result)

