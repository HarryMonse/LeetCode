from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        line = 0
        lines = 1
        for i in s:
            value = widths[alphabet.index(i)]
            line += value
            if line > 100:
                line = value
                lines += 1
        return [lines, line]
        

solution_instance = Solution()

result = solution_instance.numberOfLines(widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "abcdefghijklmnopqrstuvwxyz")
print(result)

result = solution_instance.numberOfLines(widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "bbbcccdddaaa")
print(result)