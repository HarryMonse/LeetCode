from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        salary.remove(max(salary))
        salary.remove(min(salary))
        return sum(salary)/len(salary)
    

solution_instance = Solution()

result = solution_instance.average(salary = [4000,3000,1000,2000])
print(result)

result = solution_instance.average(salary = [1000,2000,3000])
print(result)