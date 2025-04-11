class Solution:
    # Sliding Window
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = 0
        output = []

        dq = deque()
        while right < len(nums):
            if right - left < k:
                while dq and dq[-1] < nums[right]:
                    dq.pop()
                dq.append(nums[right])
                right += 1
            else:
                if dq and dq[0] == nums[left]:
                    dq.popleft()
                left += 1

            if right - left == k:
                output.append(dq[0])

        return output
