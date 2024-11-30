class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sentence = sentence.split(" ")
        s = 'a'
        l = []
        for i in sentence:
            if i[0] not in "aeiouAEIOU":
                l.append(i[1:] + i[0] + 'ma' + s)
            else:
                l.append(i + 'ma' + s)
            s += 'a'
            l.append(" ")
        l.pop()   
        return "".join(l)


solution_instance = Solution()

result = solution_instance.toGoatLatin(sentence = "I speak Goat Latin")
print(result)

result = solution_instance.toGoatLatin(sentence = "The quick brown fox jumped over the lazy dog")
print(result)