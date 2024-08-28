from typing import List


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        for i in range(len(strs)):
            if strs[i].isnumeric():
                strs[i] = int(strs[i])
            else:
                strs[i] = len(strs[i])
        return max(strs)
    

solution_instance = Solution()

result = solution_instance.maximumValue(strs = ["alic3","bob","3","4","00000"])
print(result)

result = solution_instance.maximumValue(strs = ["1","01","001","0001"])
print(result)