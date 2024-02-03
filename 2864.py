class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        one = s.count("1")
        ans = ("1"*(one-1))+("0"*(len(s)-one))+"1"
        return ans


solution_instance = Solution()

result = solution_instance.maximumOddBinaryNumber(s = "010")
print(result)

result = solution_instance.maximumOddBinaryNumber(s = "0101")
print(result)
