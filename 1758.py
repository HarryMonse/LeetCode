class Solution:
    def minOperations(self, s: str) -> int:
        odd0=0
        odd1=0
        even0=0
        even1=0
        for i in range(len(s)):
            if i%2==0:
                if s[i]=='0':
                    odd0+=1
                else:
                    odd1+=1
            else:
                if s[i]=='0':
                    even0+=1
                else:
                    even1+=1  
        return min(len(s)-odd1-even0,len(s)-even1-odd0)
        

solution_instance = Solution()

result = solution_instance.minOperations(s = "0100")
print(result)

result = solution_instance.minOperations(s = "10")
print(result)

result = solution_instance.minOperations(s = "1111")
print(result)