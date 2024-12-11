class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        res = float('inf')
        for i in target:
            c = s.count(i)//target.count(i)
            if c < res:
                res = c
        return res
    

solution_instance = Solution()

result = solution_instance.rearrangeCharacters(s = "ilovecodingonleetcode", target = "code")
print(result)

result = solution_instance.rearrangeCharacters(s = "abcba", target = "abc")
print(result)

result = solution_instance.rearrangeCharacters(s = "abbaccaddaeea", target = "aaaaa")
print(result)