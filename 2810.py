class Solution:
    def finalString(self, s: str) -> str:
        text = ""
        for i in range(len(s)):
            if s[i] != "i":
                text += s[i]
            else:
                text = text[::-1]
        return text
        

solution_instance = Solution()

result = solution_instance.finalString(s = "string")
print(result)

result = solution_instance.finalString(s = "poiinter")
print(result)
