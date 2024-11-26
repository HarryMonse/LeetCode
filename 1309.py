class Solution:
    def freqAlphabets(self, s: str) -> str:
        i=0
        st=""
        while i<len(s):
            if i+2<len(s) and s[i+2]=="#":
                st+=chr(96+int(s[i:i+2]))
                i+=2
            else:
                st+=chr(96+int(s[i]))
            i+=1
        return st
        

solution_instance = Solution()

result = solution_instance.freqAlphabets(s = "10#11#12")
print(result)

result = solution_instance.freqAlphabets(s = "1326#")
print(result)

