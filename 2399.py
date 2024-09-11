from typing import List


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        d = s[::-1]
        if len(s)%2!=0:
            return False
        else:
            for i in s:
                if (len(s)-d.index(i)-1)-s.index(i)-1 != distance[ord(i)-ord('a')]:
                    return False
            return True
        

solution_instance = Solution()

result = solution_instance.checkDistances(s = "abaccb", distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
print(result)

result = solution_instance.checkDistances(s = "aa", distance = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
print(result)