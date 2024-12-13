from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        i = 0
        for word in words: 
            if s[i:i+len(word)] != word: return False 
            i += len(word)
            if i == len(s): return True 
        return False 


solution_instance = Solution()

result = solution_instance.isPrefixString(s = "iloveleetcode", words = ["i","love","leetcode","apples"])
print(result)

result = solution_instance.isPrefixString(s = "iloveleetcode", words = ["apples","i","love","leetcode"])
print(result)

