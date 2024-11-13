from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        result = []
        s1 = s1.split()
        s2 = s2.split()
        combined = s1 + s2
        for i in combined:
            if combined.count(i) == 1:
                result.append(i)
        return result        
    

solution_instance = Solution()

result = solution_instance.uncommonFromSentences(s1 = "this apple is sweet", s2 = "this apple is sour")
print(result)

result = solution_instance.uncommonFromSentences(s1 = "apple apple", s2 = "banana")
print(result)