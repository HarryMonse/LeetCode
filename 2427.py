class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count = 0
        n = min(a, b)+1
        for i in range(1,n):
            if a % i == 0 and b % i == 0:
                count += 1
        return count


solution_instance = Solution()

result = solution_instance.commonFactors(a = 12, b = 6)
print(result)

result = solution_instance.commonFactors(a = 25, b = 30)
print(result)