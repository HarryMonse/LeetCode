from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        result = []
        
        for i in range(len(words) - 2):
            if words[i] == first and words[i + 1] == second:
                result.append(words[i + 2])
        
        return result


solution_instance = Solution()

result = solution_instance.findOcurrences(text = "alice is a good girl she is a good student", first = "a", second = "good")
print(result)

result = solution_instance.findOcurrences(text = "we will we will rock you", first = "we", second = "will")
print(result)