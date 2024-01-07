from typing import Counter, List


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        arr = []
        counter = Counter(list(set(nums1)) + list(set(nums2)) + list(set(nums3)))
        for i in counter:
            if counter[i] > 1:
                arr.append(i)
        return arr
    

solution_instance = Solution()

result = solution_instance.twoOutOfThree(nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3])
print(result)

result = solution_instance.twoOutOfThree(nums1 = [3,1], nums2 = [2,3], nums3 = [1,2])
print(result)

result = solution_instance.twoOutOfThree(nums1 = [1,2,2], nums2 = [4,3,3], nums3 = [5])
print(result)
         
        
        