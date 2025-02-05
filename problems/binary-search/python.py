class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low = 0
        high = len(nums) - 1
        while low <= high:
            length = (high + low)
            mid = math.floor(length / 2)
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                low = mid + 1
                continue
            high = mid - 1

        return -1
        