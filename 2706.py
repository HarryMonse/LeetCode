from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        price = sorted(prices)
        if price[0] + price [1] <= money:
            return money - price[0] - price[1]
        return money
        

solution_instance = Solution()

result = solution_instance.buyChoco(prices = [1,2,2], money = 3)
print(result)

result = solution_instance.buyChoco(prices = [3,2,3], money = 3)
print(result)