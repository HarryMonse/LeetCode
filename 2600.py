class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if numOnes > k:
            return k
        rem = k - numOnes - numZeros
        if rem <= 0:
            return numOnes
        return numOnes - rem
    

solution_instance = Solution()

result = solution_instance.kItemsWithMaximumSum(numOnes = 3, numZeros = 2, numNegOnes = 0, k = 2)
print(result)

result = solution_instance.kItemsWithMaximumSum(numOnes = 3, numZeros = 2, numNegOnes = 0, k = 4)
print(result)