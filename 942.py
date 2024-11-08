from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        result = []
        available_numbers = list(range(n + 1))
        stack = []
        for i in range(n + 1):
            stack.append(available_numbers[i])
            if i == n or s[i] == 'I':
                while stack:
                    result.append(stack.pop())
        return result


solution_instance = Solution()

result = solution_instance.diStringMatch(s = "IDID")
print(result)

result = solution_instance.diStringMatch(s = "III")
print(result)

result = solution_instance.diStringMatch(s = "DDI")
print(result)