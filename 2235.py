class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2


solution_instance = Solution()

result = solution_instance.sum(12,5)
print(result)

result = solution_instance.sum(-10,4)
print(result)