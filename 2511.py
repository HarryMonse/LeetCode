from typing import List


class Solution:
    def captureForts(self, forts: List[int]) -> int:
        ans = ii = 0
        for i, x in enumerate(forts):
            if x:
                if forts[ii] == -x:
                    ans = max(ans,i-ii-1)
                ii = i
        return ans
    
solution_instance = Solution()

result = solution_instance.captureForts([1,0,0,-1,0,0,0,0,1])
print(result)

result = solution_instance.captureForts([0,0,1,-1])
print(result)

        