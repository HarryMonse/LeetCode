from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        moves = 0
        for i in range(len(seats)) :
            moves += abs(seats[i] - students[i])
        return moves
    

solution_instance = Solution()

result = solution_instance.minMovesToSeat(seats = [3,1,5], students = [2,7,4])
print(result)

result = solution_instance.minMovesToSeat(seats = [4,1,5,9], students = [1,3,2,6])
print(result)

result = solution_instance.minMovesToSeat(seats = [2,2,6,6], students = [1,3,2,6])
print(result)