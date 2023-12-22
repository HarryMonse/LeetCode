class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        my_list = s.split()
        
        return len(my_list[-1])

        
solution_instance = Solution()
result = solution_instance.lengthOfLastWord("Hello World")
print(result)

solution_instance = Solution()
result = solution_instance.lengthOfLastWord("   fly me   to   the moon  ")
print(result)

solution_instance = Solution()
result = solution_instance.lengthOfLastWord("luffy is still joyboy")
print(result)




        