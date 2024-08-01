from typing import List


class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        oneDigit = sum(filter(lambda x: x < 10, nums))
        sm = sum(nums)
        return sm %2 != 0 or oneDigit != sm//2
    

solution_instance = Solution()

result = solution_instance.canAliceWin(source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20])
print(result)

result = solution_instance.canAliceWin(source = "aaaa", target = "bbbb", original = ["a","c"], changed = ["c","b"], cost = [1,2])
print(result)

result = solution_instance.canAliceWin(source = "abcd", target = "abce", original = ["a"], changed = ["e"], cost = [10000])
print(result)