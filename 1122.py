from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans=[]
        for i in arr2:
            while i in arr1:
                ans.append(i)
                arr1.remove(i)
        return ans+sorted(arr1)  


solution_instance = Solution()

result = solution_instance.relativeSortArray(arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6])
print(result)

result = solution_instance.relativeSortArray(arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6])
print(result)

