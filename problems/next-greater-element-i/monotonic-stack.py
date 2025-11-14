class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2NextGreater = [-1] * len(nums2)

        # calculate next greater elements
        stack = []
        for i in range(len(nums2) - 1, -1, -1):
            while len(stack) > 0 and nums2[i] > nums2[stack[-1]]:
                index = stack.pop()

            if len(stack) > 0:
                nums2NextGreater[i] = nums2[stack[-1]]
            stack.append(i)
        #print(nums2NextGreater)

        map = {}
        for i in range(len(nums2)):
            num2 = nums2[i]
            map[num2] = i

        output = []
        for num in nums1:
            index = map[num]
            output.append(nums2NextGreater[index])

        return output