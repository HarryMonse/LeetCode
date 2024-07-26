from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        def helper(node):

            distance = [float('inf')]*n
            distance[node] = 0
            heap = []
            heappush(heap,(0,node))
            
            while heap:
                dist,node = heappop(heap)
                for nbr,d in graph[node]:
                    if dist+d < distance[nbr] and dist+d <= distanceThreshold:
                        distance[nbr] = dist+d
                        heappush(heap, (dist+d,nbr))
            
            res = -1
            for d in distance:
                res+= d<=distanceThreshold
            return res

        graph = defaultdict(list)
        for i,j,d in edges:
            graph[i].append((j,d))
            graph[j].append((i,d))
        
        no_nodes = float('inf')
        res = 0
        for node in range(n):
            x = helper(node)
            if x <= no_nodes:
                no_nodes = x
                res = node

        return res
    

solution_instance = Solution()

result = solution_instance.findTheCity(n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4)
print(result)

result = solution_instance.findTheCity(n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2)
print(result)

