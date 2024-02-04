class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        for i in str(num):
            if num % int(i) == 0:
                count += 1
        return count
    

solution_instance = Solution()

result = solution_instance.countDigits(num = 7)
print(result)

result = solution_instance.countDigits(num = 121)
print(result)

result = solution_instance.countDigits(num = 1248)
print(result)
        