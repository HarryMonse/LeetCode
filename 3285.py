from typing import List


class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        l=[]
        for i in range(1,len(height)):
            if height[i-1]>threshold:
                l.append(i)
        return l
    

solution_instance = Solution()

result = solution_instance.stableMountains(height = [1,2,3,4,5], threshold = 2)
print(result)

result = solution_instance.stableMountains(height = [10,1,10,1,10], threshold = 3)
print(result)

result = solution_instance.stableMountains(height = [10,1,10,1,10], threshold = 10)
print(result)