from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        delete_count = 0
        for col in range(len(strs[0])):
            for row in range(1, len(strs)):
                if strs[row][col] < strs[row - 1][col]:
                    delete_count += 1
                    break 
        return delete_count
    

solution_instance = Solution()

result = solution_instance.minDeletionSize(strs = ["cba","daf","ghi"])
print(result)

result = solution_instance.minDeletionSize(strs = ["a","b"])
print(result)

result = solution_instance.minDeletionSize(strs = ["zyx","wvu","tsr"])
print(result)