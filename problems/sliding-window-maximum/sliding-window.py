class Solution:
    # Sliding Window
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = 0
        output = []

        workingMax = 0
        while right < len(nums):
            if right - left < k:
                workingMax = max(workingMax, nums[right])
                right += 1
            else:
                if workingMax == nums[left]:
                    workingMax = self.getMax(left + 1, right, nums)
                left += 1

            if right - left == k:
                output.append(workingMax)

        return output

    def getMax(self, start: int, end: int, nums: List[int]) -> int:
        output = nums[start]
        for i in range(start + 1, end):
            output = max(output, nums[i])
        return output