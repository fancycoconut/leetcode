class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        def rob_v1(nums: List[int]) -> int:
            dp = [0]

            for i in range(len(nums)):
                if i <= 1:
                    dp.append(nums[i])
                    continue

                ans = max(nums[i] + dp[i - 2], nums[i] + dp[i - 1])
                dp.append(ans)

            return max(dp[-1], dp[-2])

        a = rob_v1(nums[1:])
        b = rob_v1(nums[:-1])
        return max(a, b)
        