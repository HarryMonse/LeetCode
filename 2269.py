class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        count = 0
        n = num
        while n >= 10**(k-1):
            d = n % 10**k
            n = n // 10
            if d != 0 and num % d == 0:
                count += 1
        return count


solution_instance = Solution()

result = solution_instance.divisorSubstrings(num = 240, k = 2)
print(result)

result = solution_instance.divisorSubstrings(num = 430043, k = 2)
print(result)

