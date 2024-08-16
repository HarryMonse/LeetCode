class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        for i in range(limit + 1):
            for j in range(limit + 1):
                for k in range(limit + 1):
                    if i + j + k == n:
                        ans += 1
        return ans
    

solution_instance = Solution()

result = solution_instance.distributeCandies(n = 5, limit = 2)
print(result)

result = solution_instance.distributeCandies(n = 3, limit = 3)
print(result)
