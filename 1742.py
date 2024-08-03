class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        d=dict()
        for i in range(lowLimit,highLimit+1):
            s=str(i)
            c=0
            for i in s:
                c+=int(i)
            if(c in d):
                d[c]+=1
            else:
                d[c]=1
        return max(d.values())
    

solution_instance = Solution()

result = solution_instance.countBalls(lowLimit = 1, highLimit = 10)
print(result)

result = solution_instance.countBalls(lowLimit = 5, highLimit = 15)
print(result)

result = solution_instance.countBalls(lowLimit = 19, highLimit = 28)
print(result)