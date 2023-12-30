class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n = str(n)
        count = 0
        for i in range(len(n)):
            if i % 2 == 0:
                count += int(n[i])
            else:
                count -= int(n[i])       
        return count
    

solution_instance = Solution()

result = solution_instance.alternateDigitSum(521)
print(result)

result = solution_instance.alternateDigitSum(111)
print(result)

result = solution_instance.alternateDigitSum(886996)
print(result)


