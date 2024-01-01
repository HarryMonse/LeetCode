class Solution:
    def sortString(self, s: str) -> str:

        s = list(s)
        result = []

        while len(s) > 0:
            smallest = sorted(set(s))

            for small in smallest:
                result.append(small)
                s.remove(small)

            largest = sorted(set(s), reverse = True)

            for large in largest:
                result.append(large)
                s.remove(large)

        return ''.join(result)


solution_instance = Solution()

result = solution_instance.sortString("aaaabbbbcccc")
print(result)

result = solution_instance.sortString("rat")
print(result)
        