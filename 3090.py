class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n=len(s)
        r=0
        for i in range(n+1):
            for j in range(i+1,n+1):
                a=(s[i:j])
                c=0
                for k in a:
                    if(a.count(k)>2):
                        c+=1
                        break 
                if(c==0):
                    r=max(r,len(a))
        return(r)
    

solution_instance = Solution()

result = solution_instance.maximumLengthSubstring(s = "bcbbbcba")
print(result)

result = solution_instance.maximumLengthSubstring(s = "aaaa")
print(result)

