class Solution:
    def sumBase(self, n: int, k: int) -> int:
        a = 0
        while n!=0:
            if n//k:
                a+=n%k
                n//=k
            else:
                a+=n
                n=0
        return a
    

solution_instance = Solution()

result = solution_instance.sumBase(n = 34, k = 6)
print(result)

result = solution_instance.sumBase(n = 10, k = 10)
print(result)

