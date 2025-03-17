class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [ False for _ in nums ]
        dp[-1] = True
        
        for i in range(len(nums) - 2, -1, -1):
            num = nums[i]
            longestJump = min(i + num, len(nums) - 1)
            print(longestJump)

            for j in range(i + 1, longestJump + 1):
                if dp[j] == True:
                    dp[i] = dp[j]
                    break

        print(dp)
        return dp[0]
