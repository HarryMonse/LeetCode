from collections import defaultdict
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        length=0
        check=0
        freq= defaultdict(int)
        for c in chars:
            freq[c]+=1
        for i in words:
            check=0
            for j in i:
                if i.count(j)>freq[j]:
                    check=1
            if check==0:
                length=length+len(i) 
        return(length)
    

solution_instance = Solution()

result = solution_instance.countCharacters(words = ["cat","bt","hat","tree"], chars = "atach")
print(result)

result = solution_instance.countCharacters(words = ["hello","world","leetcode"], chars = "welldonehoneyr")
print(result)

