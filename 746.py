from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(len(cost)-3,-1,-1):
            cost[i]=min(cost[i]+cost[i+1],cost[i]+cost[i+2])
        return min(cost[0],cost[1])


solution_instance = Solution()

result = solution_instance.minCostClimbingStairs(cost = [10,15,20])
print(result)

result = solution_instance.minCostClimbingStairs(cost = [1,100,1,1,1,100,1,1,100,1])
print(result)

