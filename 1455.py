class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        for i, word in enumerate(words, 1):
            if word.startswith(searchWord):
                return i
        return -1
    

solution_instance = Solution()

result = solution_instance.isPrefixOfWord(sentence = "i love eating burger", searchWord = "burg")
print(result)

result = solution_instance.isPrefixOfWord(sentence = "this problem is an easy problem", searchWord = "pro")
print(result)

result = solution_instance.isPrefixOfWord(sentence = "i am tired", searchWord = "you")
print(result)