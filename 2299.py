class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        check1 = len(password) >= 8
        check2 = any([i.islower() for i in password])
        check3 = any([i.isupper() for i in password])
        check4 = any([i.isdigit() for i in password])
        check5 = any([i in '!@#$%^&*()-+' for i in password])
        check6 = True
        for i in range(len(password)-1):
          if password[i] == password[i+1]:
            check6 = False
            break
        checks = [check1,check2,check3,check4,check5,check6]
        return all(checks)


solution_instance = Solution()

result = solution_instance.strongPasswordCheckerII(password = "IloveLe3tcode!")
print(result)

result = solution_instance.strongPasswordCheckerII(password = "Me+You--IsMyDream")
print(result)

result = solution_instance.strongPasswordCheckerII(password = "1aB!")
print(result)