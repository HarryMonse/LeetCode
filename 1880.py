class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        x=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        a=""
        for i in firstWord:
            a=a+str(x.index(i))
        
        b=""
        for i in secondWord:
            b=b+str(x.index(i))

        c=""
        for i in targetWord:
            c=c+str(x.index(i))
        if int(a)+int(b)==int(c):
            return True
        return False


solution_instance = Solution()

result = solution_instance.isSumEqual(firstWord = "acb", secondWord = "cba", targetWord = "cdb")
print(result)

result = solution_instance.isSumEqual(firstWord = "aaa", secondWord = "a", targetWord = "aab")
print(result)

result = solution_instance.isSumEqual(firstWord = "aaa", secondWord = "a", targetWord = "aaaa")
print(result)