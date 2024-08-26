from collections import Counter


class Solution:
    def countLargestGroup(self, n: int) -> int:
        cases = [sum([int(digit) for digit in str(i)]) for i in range(1,n+1)]
        c = Counter(cases)
        max_size = max(c.values())
        return list(c.values()).count(max_size)
        

solution_instance = Solution()

result = solution_instance.countLargestGroup(n = 13)
print(result)

result = solution_instance.countLargestGroup(n = 2)
print(result)

