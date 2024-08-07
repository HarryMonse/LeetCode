class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = 0
        for i in range(n):
            res ^= start + 2 * i
        return res
    

solution_instance = Solution()

result = solution_instance.xorOperation(n = 5, start = 0)
print(result)

result = solution_instance.xorOperation(n = 4, start = 3)
print(result)
