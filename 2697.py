class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        for i in range(int(len(s)/2)):
            if s[i] != s[len(s)-i-1]:
                if s[i] < s[len(s)-i-1]:
                    s = s[:len(s)-i-1] + s[i] + s[len(s)-i:]
                else:
                    s = s[:i] + s[len(s)-i-1] + s[i+1:]
        return s
    

solution_instance = Solution()

result = solution_instance.makeSmallestPalindrome(s = "egcfe")
print(result)

result = solution_instance.makeSmallestPalindrome(s = "abcd")
print(result)

result = solution_instance.makeSmallestPalindrome(s = "seven")
print(result)

