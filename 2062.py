class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        fin=0
        for i in range(len(word)):             
            seen = set()
            for j in range(i,len(word)):
                if word[j] in 'aeiou':
                    seen.add(word[j])
                    if len(seen)>=5:
                        fin+=1
                else:
                    break                
        return fin
    

solution_instance = Solution()

result = solution_instance.countVowelSubstrings(word = "aeiouu")
print(result)

result = solution_instance.countVowelSubstrings(word = "unicornarihan")
print(result)

result = solution_instance.countVowelSubstrings(word = "cuaieuouac")
print(result)