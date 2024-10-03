from typing import Counter, List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = []
        for i in logs:
            for j in range(i[0],i[1]):
                years.append(j)
        result = Counter(years)
        max_count = max(result.values())
        ans = min(num for num, freq in result.items() if freq == max_count)
        return ans
    

solution_instance = Solution()

result = solution_instance.maximumPopulation(logs = [[1993,1999],[2000,2010]])
print(result)

result = solution_instance.maximumPopulation(logs = [[1950,1961],[1960,1971],[1970,1981]])
print(result)
        
