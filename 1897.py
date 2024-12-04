from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n=len(words)
        ans=''.join(words)
        res=set(ans)
        for i in res:
            if ans.count(i)%n!=0:
                return False
        return True     


solution_instance = Solution()

result = solution_instance.makeEqual(words = ["abc","aabc","bc"])
print(result)

result = solution_instance.makeEqual(words = ["ab","a"])
print(result)

