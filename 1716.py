class Solution:
    def totalMoney(self, n: int) -> int:
        count = 0  # value that gets added to the list
        end = 0   # value to keep track when the value of n becomes multiple of 7 (for every monday)
        start = 1 # to keep track of the value to be increased for each subsequent monday
        answerList = [] # list that contains the answer values
        for i in range(n):
            count = count + 1
            end = end + 1
            if end % 7 == 0:
                answerList.append(count)
                start = start + 1
                count = start - 1
                end = 0
            else:
                answerList.append(count)

        return sum(answerList)


solution_instance = Solution()

result = solution_instance.totalMoney(n = 4)
print(result)

result = solution_instance.totalMoney(n = 10)
print(result)

result = solution_instance.totalMoney(n = 20)
print(result)