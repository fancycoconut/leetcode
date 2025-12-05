class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < len(nums) and left != right and right >= 0:
            a = nums[left]
            b = nums[right]

            if b == val:
                right -= 1
                continue
            if a == val:
                nums[left] = nums[left] ^ nums[right]
                nums[right] = nums[left] ^ nums[right]
                nums[left] = nums[left] ^ nums[right]
                #numOfElementsRemoved += 1
                right -= 1
                continue
            left += 1
        print(nums)
        
        numOfElementsRemoved = 0
        for num in nums:
            if num == val:
                numOfElementsRemoved += 1
        print(numOfElementsRemoved)
            
        return len(nums) - numOfElementsRemoved