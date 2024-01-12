class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        temp = '01'
        while temp in s:
            temp = '0' + temp + '1'
        return len(temp) - 2
    

solution_instance = Solution()

result = solution_instance.findTheLongestBalancedSubstring(s = "01000111")
print(result)

result = solution_instance.findTheLongestBalancedSubstring(s = "00111")
print(result)

result = solution_instance.findTheLongestBalancedSubstring(s = "111")
print(result)

        