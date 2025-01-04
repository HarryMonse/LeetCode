from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1],reverse=1)
        s=0
        for i,j in boxTypes:
            i=min(i,truckSize)
            s+=i*j
            truckSize-=i
            if truckSize==0:
                break
        return s


solution_instance = Solution()

result = solution_instance.maximumUnits(boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4)
print(result)

result = solution_instance.maximumUnits(boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10)
print(result)

