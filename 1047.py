class Solution:
    def removeDuplicates(self, s: str) -> str:
        lis=[s[0]]
        for i in range(1,len(s)):
            if len(lis)==0 or lis[len(lis)-1]!=s[i]:
                lis.append(s[i])
            else:
                lis=lis[:len(lis)-1]        
        s="".join(lis)
        return s    


solution_instance = Solution()

result = solution_instance.removeDuplicates(s = "abbaca")
print(result)

result = solution_instance.removeDuplicates(s = "azxxzy")
print(result)


