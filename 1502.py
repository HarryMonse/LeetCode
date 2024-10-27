from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(1,len(arr)-1):
            if arr[i-1]-arr[i]!=arr[i]-arr[i+1]:
                return False
        return True


solution_instance = Solution()

result = solution_instance.canMakeArithmeticProgression(arr = [3,5,1])
print(result)

result = solution_instance.canMakeArithmeticProgression(arr = [1,2,4])
print(result)

