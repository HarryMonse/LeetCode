class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        ans = [''] * n
        for i in range(n):
            ans[i] = s[(i + k) % n]
        return ''.join(ans) 
    

solution_instance = Solution()

result = solution_instance.getEncryptedString(s = "dart", k = 3)
print(result)

result = solution_instance.getEncryptedString(s = "aaa", k = 1)
print(result)