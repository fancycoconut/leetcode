class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right - left) // 2
            i = left + mid
            if nums[i] == target:
                return i

            # Subarray on the mid's left is sorted
            if nums[i] >= nums[left]:
                if target >= nums[left] and target < nums[i]:
                    right = i - 1
                else:
                    left = i + 1
            # Subarray on the mid's right is sorted
            else:
                if target <= nums[right] and target > nums[i]:
                    left = i + 1
                else:
                    right = i - 1
        return -1