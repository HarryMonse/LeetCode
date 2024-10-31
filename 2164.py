from typing import List


class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even, odd = [], []
        for i, n in enumerate(nums):
            if i % 2 == 0:
                even.append(n)
            else:
                odd.append(n)
        even.sort()
        odd.sort(reverse=True)
        new = []
        for i, e in enumerate(even):
            new.append(even[i])
            if i < len(odd):
                new.append(odd[i])
        return new


solution_instance = Solution()

result = solution_instance.sortEvenOdd(nums = [4,1,2,3])
print(result)

result = solution_instance.sortEvenOdd(nums = [2,1])
print(result)