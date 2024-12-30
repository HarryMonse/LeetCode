from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        rank_mapping = {score: medals[i] if i < 3 else str(i + 1) for i, score in enumerate(sorted_score)}
        return [rank_mapping[score] for score in score]


solution_instance = Solution()

result = solution_instance.findRelativeRanks(score = [5,4,3,2,1])
print(result)

result = solution_instance.findRelativeRanks(score = [10,3,8,9,4])
print(result)