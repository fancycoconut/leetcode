class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        numOfEvenDiffPartitions = 0

        for marker in range(1, len(nums)):
            leftPartitionSum = sum(nums[0:marker])
            rightPartitionSum = sum(nums[marker:])

            diff = leftPartitionSum - rightPartitionSum
            if diff % 2 == 0:
                numOfEvenDiffPartitions += 1
        return numOfEvenDiffPartitions
