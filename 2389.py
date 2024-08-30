from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        numsSorted = sorted(nums)
        res = []
		
        for q in queries:
            total = 0
            count = 0
            for num in numsSorted:
                total += num
                count += 1
                if total > q:
                    count -= 1
                    break
            res.append(count)
        
        return res
    

solution_instance = Solution()

result = solution_instance.answerQueries(nums = [4,5,2,1], queries = [3,10,21])
print(result)

result = solution_instance.answerQueries(nums = [2,3,4,5], queries = [1])
print(result)
