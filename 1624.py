class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans=-1
        for x,a in enumerate(s):
            for y,b in enumerate(s):
                if a==b and x!=y:
                    ans=max(ans,abs(x-y)-1)
        return ans


solution_instance = Solution()

result = solution_instance.maxLengthBetweenEqualCharacters(s = "aa")
print(result)

result = solution_instance.maxLengthBetweenEqualCharacters(s = "abca")
print(result)

result = solution_instance.maxLengthBetweenEqualCharacters(s = "cbzxy")
print(result)