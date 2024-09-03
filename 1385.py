from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        cnt = 0
        for i in arr1:
            flag = 0
            for j in arr2:
                if abs(i-j) <= d:
                    flag = 1
                    break
            if flag == 0:
                cnt += 1
        return cnt
    

solution_instance = Solution()

result = solution_instance.findTheDistanceValue(arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2)
print(result)

result = solution_instance.findTheDistanceValue(arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3)
print(result)

result = solution_instance.findTheDistanceValue(arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6)
print(result)