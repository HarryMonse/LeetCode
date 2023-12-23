class Solution:
    def largestOddNumber(self, num: str) -> str:
        n=len(num)
        ans=n-1
        while ans>=0 and int(num[ans])%2==0:
            ans-=1

        if ans<0:
            return ""
        return num[:ans+1]        
    

solution_instance = Solution()

result = solution_instance.largestOddNumber("52")
print(result)

result = solution_instance.largestOddNumber("4206")
print(result)

result = solution_instance.largestOddNumber("35427")
print(result)