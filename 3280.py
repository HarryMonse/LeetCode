class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return '-'.join(bin(int(x))[2:] for x in date.split('-'))
    

solution_instance = Solution()

result = solution_instance.convertDateToBinary(date = "2080-02-29")
print(result)

result = solution_instance.convertDateToBinary(date = "1900-01-01")
print(result)