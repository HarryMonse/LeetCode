class Solution:
    def makeGood(self, s: str) -> str:
        stack = []  
        for char in s:
            if stack and abs(ord(char) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)
    

solution_instance = Solution()

result = solution_instance.makeGood(s = "leEeetcode")
print(result)

result = solution_instance.makeGood(s = "abBAcC")
print(result)

result = solution_instance.makeGood(s = "s")
print(result)