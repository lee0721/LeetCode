class Solution:
    def climbStairs(self, n: int) -> int:
        first, second = 1, 2
        if n == first: return first
        if n == second: return second

        for i in range(3, n+1):
            third = first + second
            first = second
            second = third
        return third