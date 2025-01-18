# 1. Define the objective function
# f(n) => the number of distinct ways to reach the n-th stair
# 2. Identity base cases
# f(0) = 1
# f(1) = 1
# 3. Recurrence relation:
# f(n) = f(n - 1) + f(n - 2) 
# 4. Order of computation
# bottom-up
# 5. Location of the answer
# f(n)
class Solution:
    cache = {}

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n in self.cache.keys():
            return self.cache[n]
        
        result = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self.cache[n] = result
        return result
        