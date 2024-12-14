class Solution:
    def possibleStringCount(self, word: str) -> int:
        n=len(word)
        count=1
        for i in range(n):
            if i+1<n and word[i]==word[i+1]:
                count+=1
        return count
    

solution_instance = Solution()

result = solution_instance.possibleStringCount(word = "abbcccc")
print(result)

result = solution_instance.possibleStringCount(word = "abcd")
print(result)

result = solution_instance.possibleStringCount(word = "aaaa")
print(result)

