class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        return sorted_s == sorted(t)
        

solution_instance = Solution()

result = solution_instance.isAnagram(s = "anagram", t = "nagaram")
print(result)

result = solution_instance.isAnagram(s = "rat", t = "car")
print(result)