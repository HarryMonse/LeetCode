class Solution:
    def digitSum(self, s: str, k: int) -> str:
        s = list(map(int, s))
        while len(s) > k:
            tmp = []
            for i in range(0, len(s), k):
                S = sum(s[i:i+k])
                for d in (str(S)):
                    tmp.append(int(d))
            s = tmp

        return ''.join(map(str, s))


solution_instance = Solution()

result = solution_instance.digitSum(s = "11111222223", k = 3)
print(result)

result = solution_instance.digitSum(s = "00000000", k = 3)
print(result)

