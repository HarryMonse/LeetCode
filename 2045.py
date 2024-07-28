from collections import defaultdict
from heapq import heappop, heappush
import sys
from typing import List


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        dist1 = [sys.maxsize] * (n + 1)
        dist2 = [sys.maxsize] * (n + 1)
        freq = [0] * (n + 1)
        min_heap = [(0, 1)]
        dist1[1] = 0

        while min_heap:
            timeTaken, node = heappop(min_heap)
            freq[node] += 1

            if freq[node] == 2 and node == n:
                return timeTaken
            
            if (timeTaken // change) % 2 == 1:
                timeTaken = change * (timeTaken // change + 1) + time
            else:
                timeTaken += time
            
            for neighbor in adj[node]:
                if freq[neighbor] == 2:
                    continue

                if dist1[neighbor] > timeTaken:
                    dist2[neighbor] = dist1[neighbor]
                    dist1[neighbor] = timeTaken
                    heappush(min_heap, (timeTaken, neighbor))
                elif dist2[neighbor] > timeTaken and dist1[neighbor] != timeTaken:
                    dist2[neighbor] = timeTaken
                    heappush(min_heap, (timeTaken, neighbor))
        
        return 0
    

solution_instance = Solution()

result = solution_instance.secondMinimum(n = 5, edges = [[1,2],[1,3],[1,4],[3,4],[4,5]], time = 3, change = 5)
print(result)

result = solution_instance.secondMinimum(n = 2, edges = [[1,2]], time = 3, change = 2)
print(result)