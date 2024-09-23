from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ans = []
        for row in image:
            flipped_row = row[::-1]
            inverted_row = [1 - x for x in flipped_row]
            ans.append(inverted_row)
        return ans
    

solution_instance = Solution()

result = solution_instance.flipAndInvertImage(image = [[1,1,0],[1,0,1],[0,0,0]])
print(result)

result = solution_instance.flipAndInvertImage(image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]])
print(result)