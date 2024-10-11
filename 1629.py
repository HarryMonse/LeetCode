from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        maxi = releaseTimes[0] 
        lar = keysPressed[0]  
        n = len(releaseTimes) 
        for i in range(1, n):
            diff = releaseTimes[i] - releaseTimes[i - 1]  
            if diff > maxi or (diff == maxi and keysPressed[i] > lar):
                maxi = diff  
                lar = keysPressed[i]  
        return lar  


solution_instance = Solution()

result = solution_instance.slowestKey(releaseTimes = [9,29,49,50], keysPressed = "cbcd")
print(result)

result = solution_instance.slowestKey(releaseTimes = [12,23,36,46,62], keysPressed = "spuda")
print(result)

