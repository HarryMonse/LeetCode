from typing import List


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        dp = [[float('inf')] * 26 for _ in range(26)]
        for i in range(26):
            dp[i][i] = 0
        for old, new, c in zip(original, changed, cost):
            old, new = ord(old) - ord('a'), ord(new) - ord('a')
            dp[old][new] = min(dp[old][new], c)
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
        res = sum(dp[ord(s) - ord('a')][ord(t) - ord('a')] for s, t in zip(source, target))
        return res if res != float('inf') else -1


solution_instance = Solution()

result = solution_instance.minimumCost(source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20])
print(result)

result = solution_instance.minimumCost(source = "aaaa", target = "bbbb", original = ["a","c"], changed = ["c","b"], cost = [1,2])
print(result)

result = solution_instance.minimumCost(source = "abcd", target = "abce", original = ["a"], changed = ["e"], cost = [10000])
print(result)


