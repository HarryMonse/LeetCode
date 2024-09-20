class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums = []
        words = s.split()
        for word in words:
            if word.isdigit():
                nums.append(int(word))
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                return False
        return True


solution_instance = Solution()

result = solution_instance.areNumbersAscending(s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles")
print(result)

result = solution_instance.areNumbersAscending(s = "hello world 5 x 5")
print(result)

result = solution_instance.areNumbersAscending(s = "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s")
print(result)