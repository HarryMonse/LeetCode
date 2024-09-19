class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        countA = 0
        countB = 0
        vowels = "aeiouAEIOU"
        l = len(s)//2
        a = s[:l]
        b = s[l:]
        for i in a:
            if i in vowels:
                countA += 1
        for i in b:
            if i in vowels:
                countB += 1
        return countA == countB
        

solution_instance = Solution()

result = solution_instance.halvesAreAlike(s = "book")
print(result)

result = solution_instance.halvesAreAlike(s = "textbook")
print(result)
