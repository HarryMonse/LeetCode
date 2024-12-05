class Solution:
    def interpret(self, command: str) -> str:
        str1 = ""
        for i in command:
            str1 = str1 + i
        return(str1.replace("()","o").replace("(al)","al"))


solution_instance = Solution()

result = solution_instance.interpret(command = "G()(al)")
print(result)

result = solution_instance.interpret(command = "G()()()()(al)")
print(result)

result = solution_instance.interpret(command = "(al)G(al)()()G")
print(result)