class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        num = num[::-1]
        num = int(num)
        num = str(num)
        num = num[::-1]
        return num


solution_instance = Solution()

result = solution_instance.removeTrailingZeros(num = "51230100")
print(result)

result = solution_instance.removeTrailingZeros(num = "123")
print(result)
        