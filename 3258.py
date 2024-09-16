class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0

        for i in range(n):
            zero_count, one_count = 0, 0
            for j in range(i, n):
                if s[j] == '0':
                    zero_count += 1
                else:
                    one_count += 1
                
                if zero_count <= k or one_count <= k:
                    ans += 1

        return ans
    

solution_instance = Solution()

result = solution_instance.countKConstraintSubstrings(s = "10101", k = 1)
print(result)

result = solution_instance.countKConstraintSubstrings(s = "1010101", k = 2)
print(result)

result = solution_instance.countKConstraintSubstrings(s = "11111", k = 1)
print(result)