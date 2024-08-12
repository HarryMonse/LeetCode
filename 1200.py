from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        indx = []
        arr.sort()
        mabs = arr[1] - arr[0]
        for i in range(len(arr) - 1):
            min_abs = abs(arr[i + 1] - arr[i])

            if min_abs < mabs:
                mabs = min_abs
                indx.clear()
                indx.append([arr[i], arr[i + 1]])

            elif min_abs == mabs:
                indx.append([arr[i], arr[i + 1]])

        return indx
    

solution_instance = Solution()

result = solution_instance.minimumAbsDifference(arr = [4,2,1,3])
print(result)

result = solution_instance.minimumAbsDifference(arr = [1,3,6,10,15])
print(result)

result = solution_instance.minimumAbsDifference(arr = [3,8,-10,23,19,-4,-14,27])
print(result)
    