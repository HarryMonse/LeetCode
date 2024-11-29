class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        one_list = s.split("0")
        zero_list = s.split("1")
        
        one_max = max(one_list, key=len)
        zero_max = max(zero_list, key=len)
        
        if len(one_max) > len(zero_max):
            return True
        else:
            return False
        

solution_instance = Solution()

result = solution_instance.checkZeroOnes(s = "1101")
print(result)

result = solution_instance.checkZeroOnes(s = "111000")
print(result)

result = solution_instance.checkZeroOnes(s = "110100010")
print(result)