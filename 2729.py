class Solution:
    def isFascinating(self, n: int) -> bool:
        conc = str(n) + str(2 * n) + str(3 * n)
        if "0" in conc:
            return False
        if len(conc) > 9:
            return False
        for i in range(1,10):
            if str(i) not in conc:
                return False
        return True


solution_instance = Solution()

result = solution_instance.isFascinating(n = 192)
print(result)

result = solution_instance.isFascinating(n = 100)
print(result)


        