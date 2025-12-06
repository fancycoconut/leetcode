class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        # Find pivot point ie. smallest element
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1
        print(left)

        def binarySearch(leftBoundary: int, rightBoundary: int, target: int) -> int:
            left = leftBoundary
            right = rightBoundary

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        if (answer := binarySearch(0, left - 1, target)) != -1:
            return answer

        return binarySearch(left, len(nums) - 1, target)