from typing import List


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate = ''.join([i.lower() for i in licensePlate if i.isalpha()])
        words = sorted(words, key=len)
        for word in words:
            for i in range(len(licensePlate)):
                if word.count(licensePlate[i]) < licensePlate.count(licensePlate[i]):
                    break
                if i == len(licensePlate)-1:
                    return word


solution_instance = Solution()

result = solution_instance.shortestCompletingWord(licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"])
print(result)

result = solution_instance.shortestCompletingWord(licensePlate = "1s3 456", words = ["looks","pest","stew","show"])
print(result)