from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        flag = 0
        while flag < len(sandwiches):
            if not students:
                return True
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                flag = 0
            else:
                students.append(students.pop(0))
                flag += 1
        return len(sandwiches)


solution_instance = Solution()

result = solution_instance.countStudents(students = [1,1,0,0], sandwiches = [0,1,0,1])
print(result)

result = solution_instance.countStudents(students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1])
print(result)