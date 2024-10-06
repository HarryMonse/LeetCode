from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result = []
        for i in range(100, 1000, 2):
            temp = str(i)
            for j in temp:
                if int(j) in digits:
                    if temp.count(j) > digits.count(int(j)):
                        break
                else:
                    break
            else:
                result.append(i)
        return result
                         

solution_instance = Solution()

result = solution_instance.findEvenNumbers(digits = [2,1,3,0])
print(result)

result = solution_instance.findEvenNumbers(digits = [2,2,8,8,2])
print(result)

result = solution_instance.findEvenNumbers(digits = [3,7,5])
print(result)
