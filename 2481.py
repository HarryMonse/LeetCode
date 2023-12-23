class Solution:
    def numberOfCuts(self, n: int) -> int:

        if n == 1:
            return 0
        return n // 2 if n % 2 == 0 else n 


solution_instance = Solution()

result = solution_instance.numberOfCuts(4)
print(result)

result = solution_instance.numberOfCuts(3)
print(result)