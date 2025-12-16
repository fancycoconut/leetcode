class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        output = [-1] * len(nums)
        stack = []

        n = len(nums)
        # Calculate next greater elements in the circular array by looping twice
        for i in range(2 * n - 1, -1, -1):
            j = i % len(nums)
            while len(stack) > 0 and nums[j] >= stack[-1]:
                stack.pop()

            if len(stack) > 0:
                output[j] = stack[-1]
            stack.append(nums[j])

        return output
