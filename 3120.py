class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        l=[]
        c=0
        word=list(set(word))
        s0='QWERTYUIOPASDFGHJKLZXCVBNM'
        s1='qwertyuiopasdfghjklzxcvbnm'
        for i in word:
            if i in s1 and  i.upper() in l:
                c+=1
            if i in s0 and i.lower() in l:
                c+=1
            else:
                l.append(i)
        return c


solution_instance = Solution()

result = solution_instance.numberOfSpecialChars(word = "aaAbcBC")
print(result)

result = solution_instance.numberOfSpecialChars(word = "abc")
print(result)

result = solution_instance.numberOfSpecialChars(word = "abBCab")
print(result)