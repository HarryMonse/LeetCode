class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num_str = ''.join(str(ord(char) - ord('a') + 1) for char in s)
        for _ in range(k):
            num_str = sum(int(digit) for digit in num_str)
            num_str = str(num_str)
        return(int(num_str))
    

solution_instance = Solution()

result = solution_instance.getLucky(s = "iiii", k = 1)
print(result)

result = solution_instance.getLucky(s = "leetcode", k = 2)
print(result)

result = solution_instance.getLucky(s = "zbax", k = 2)
print(result)