class Solution:
    def minLength(self, s: str) -> int:
        while "AB" in s or "CD" in s:
            if "AB" in s:
                s = s.replace("AB","")
            elif "CD" in s:
                s = s.replace("CD","")
        return len(s)


solution_instance = Solution()

result = solution_instance.minLength(s = "ABFCACDB")
print(result)

result = solution_instance.minLength(s = "ACBBD")
print(result)
                
        