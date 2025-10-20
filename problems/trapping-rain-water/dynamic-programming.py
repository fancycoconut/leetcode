class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        leftMaxHeights = [0] * len(height)
        rightMaxHeights = [0] * len(height)

        leftMaxHeights[0] = height[0]
        for i in range(1, len(height)):
            leftMaxHeights[i] = max(height[i], leftMaxHeights[i - 1])
        
        rightMaxHeights[-1] = height[-1]        
        for i in range(len(height) - 2, -1, -1):
            rightMaxHeights[i] = max(height[i], rightMaxHeights[i + 1])

        totalWaterTrapped = 0
        for i in range(len(height)):
            h = height[i]
            waterTrapped = min(leftMaxHeights[i], rightMaxHeights[i]) - h
            totalWaterTrapped += waterTrapped
            print("pos: " + str(i) + " max left: " + str(leftMaxHeights[i]) + " max right: " + str(rightMaxHeights[i]))

        return totalWaterTrapped
