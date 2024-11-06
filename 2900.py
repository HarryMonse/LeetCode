from typing import List


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        i = 0
        n = len(words)
        ans = []
        while i < n:
            ans.append(words[i])
            while i < n-1 and groups[i] == groups[i+1]:
                i += 1
            i += 1
        return ans
    

solution_instance = Solution()

result = solution_instance.getLongestSubsequence(words = ["e","a","b"], groups = [0,0,1])
print(result)

result = solution_instance.getLongestSubsequence(words = ["a","b","c","d"], groups = [1,0,1,1])
print(result)