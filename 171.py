class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            result = result * 26 + (ord(char) - ord('A') + 1)
        return result


solution_instance = Solution()

result = solution_instance.titleToNumber(columnTitle = "A")
print(result)

result = solution_instance.titleToNumber(columnTitle = "AB")
print(result)

result = solution_instance.titleToNumber(columnTitle = "ZY")
print(result)

