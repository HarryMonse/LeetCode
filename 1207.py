from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = [] 
        for i in arr:
            c.append(arr.count(i))
        return len(set(c)) == len(set(arr))


solution_instance = Solution()

result = solution_instance.uniqueOccurrences(arr = [1,2,2,1,1,3])
print(result)

result = solution_instance.uniqueOccurrences(arr = [1,2])
print(result)

result = solution_instance.uniqueOccurrences(arr = [-3,0,1,-3,1,1,1,-3,10,0])
print(result)
    

        
        