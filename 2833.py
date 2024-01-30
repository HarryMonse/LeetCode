class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l = moves.count("L")
        r = moves.count("R")
        s = moves.count("_")
        return abs(l-r) + s


solution_instance = Solution()

result = solution_instance.furthestDistanceFromOrigin(moves = "L_RL__R")
print(result)

result = solution_instance.furthestDistanceFromOrigin(moves = "_R__LL_")
print(result)

result = solution_instance.furthestDistanceFromOrigin(moves = "_______")
print(result)
