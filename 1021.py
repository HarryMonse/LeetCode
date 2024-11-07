class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ''
        cnt = 0
        for ch in s:
            if ch == '(':
                if cnt:
                    ans += ch
                cnt += 1
            else:
                cnt -= 1
                if cnt:
                    ans += ch
        return ans


solution_instance = Solution()

result = solution_instance.removeOuterParentheses(s = "(()())(())")
print(result)

result = solution_instance.removeOuterParentheses(s = "(()())(())(()(()))")
print(result)

result = solution_instance.removeOuterParentheses(s = "()()")
print(result)