class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if (sentence[0] != sentence[-1]):
            return False
    
        for index in range(len(sentence)):
            if sentence[index] == " ":
                if (sentence[index-1] != sentence[index+1])  :
                    return False 

        return True 
                

solution_instance = Solution()

result = solution_instance.isCircularSentence(sentence = "leetcode exercises sound delightful")
print(result)

result = solution_instance.isCircularSentence(sentence = "eetcode")
print(result)

result = solution_instance.isCircularSentence(sentence = "Leetcode is cool")
print(result)