from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_element = -1 
        for i in range(len(arr)-1, -1, -1):
            temp = max_element
            max_element = max(arr[i], max_element)
            arr[i] = temp
        return arr
            
        
solution_instance = Solution()

result = solution_instance.replaceElements(arr = [17,18,5,4,6,1])
print(result)

result = solution_instance.replaceElements(arr = [400])
print(result)


