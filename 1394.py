from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        my_list = []
        for i in arr:
            if arr.count(i) == i:
                my_list.append(i)
        if len(my_list) == 0:
            return -1
        else:
            return max(my_list)


solution_instance = Solution()

result = solution_instance.findLucky(arr = [2,2,3,4])
print(result)

result = solution_instance.findLucky(arr = [1,2,2,3,3,3])
print(result)

result = solution_instance.findLucky(arr = [2,2,2,3,3])
print(result)
        

        