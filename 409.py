class Solution:
    def longestPalindrome(self, s: str) -> int:
        ss = set()
        for letter in s:
            if letter not in ss:
                ss.add(letter)
            else:
                ss.remove(letter)
        if len(ss) != 0:
            return len(s) - len(ss) + 1
        else:
            return len(s)


solution_instance = Solution()

result = solution_instance.longestPalindrome(s = "abccccdd")
print(result)

result = solution_instance.longestPalindrome(s = "a")
print(result)

