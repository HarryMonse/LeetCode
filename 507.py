class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num==1:
            return False
        count=1
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                count+=i+num//i
        return num==count


solution_instance = Solution()

result = solution_instance.checkPerfectNumber(28)
print(result)

result = solution_instance.checkPerfectNumber(7)
print(result)