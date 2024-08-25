class Solution:
    def divisorGame(self, n: int) -> bool:
        if n % 2 == 0:
            return True
        else:
            return False
        

solution_instance = Solution()

result = solution_instance.divisorGame(n = 2)
print(result)

result = solution_instance.divisorGame(n = 3)
print(result)