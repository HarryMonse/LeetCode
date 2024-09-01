class Solution:
    def replaceDigits(self, s: str) -> str:
        new=""
        for i in range(len(s)):
            if i%2==0:
                new+=s[i]
            else:
                new+=chr(ord(s[i-1])+int(s[i]))
        return new
    

solution_instance = Solution()

result = solution_instance.replaceDigits(s = "a1c1e1")
print(result)

result = solution_instance.replaceDigits(s = "a1b2c3d4e")
print(result)

