class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = title.split()
        for i in range(len(title)):
            word = title[i]
            if len(word) < 3:
                title[i] = word.lower()
            else:
                title[i] = word.title()
        return " ".join(title)


solution_instance = Solution()

result = solution_instance.capitalizeTitle(title = "capiTalIze tHe titLe")
print(result)

result = solution_instance.capitalizeTitle(title = "First leTTeR of EACH Word")
print(result)

result = solution_instance.capitalizeTitle(title = "i lOve leetcode")
print(result)