class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        memo = []
        memo.append(0)
        for i in range(0, len(nums)):
            if i <= 1:
                memo.append(nums[i])
                continue

            ans = max(memo[i - 2] + nums[i], memo[i - 1] + nums[i])
            memo.append(ans)

        print(memo)
        return max(memo[-1], memo[-2])
