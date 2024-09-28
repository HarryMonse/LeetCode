class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        num1, num2, num3 = str(num1), str(num2), str(num3)
        if len(num1) < 4:
            num1 = (4 - len(num1)) * "0" + num1
        if len(num2) < 4:
            num2 = (4 - len(num2)) * "0" + num2
        if len(num3) < 4:
            num3 = (4 - len(num3)) * "0" + num3
        out = ''
        for i in range(4):
            out += str(min(int(num1[i]), int(num2[i]), int(num3[i])))
        return int(out)


solution_instance = Solution()

result = solution_instance.generateKey(num1 = 1, num2 = 10, num3 = 1000)
print(result)

result = solution_instance.generateKey(num1 = 987, num2 = 879, num3 = 798)
print(result)

result = solution_instance.generateKey(num1 = 1, num2 = 2, num3 = 3)
print(result)