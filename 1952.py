class Solution:
    def isThree(self, n: int) -> bool:
        count = 0
        for i in range(1,n+1):
            if n % i == 0:
                count += 1
        return count == 3 


solution_instance = Solution()

result = solution_instance.isThree(n = 2)
print(result)

result = solution_instance.isThree(n = 4)
print(result)

        