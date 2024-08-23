class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        difference = 0
        for char in set(s):
            index_s = s.index(char)
            index_t = t.index(char)
            difference += abs(index_s - index_t)
        return difference
    

solution_instance = Solution()

result = solution_instance.findPermutationDifference(s = "abc", t = "bac")
print(result)

result = solution_instance.findPermutationDifference(s = "abcde", t = "edbac")
print(result)

