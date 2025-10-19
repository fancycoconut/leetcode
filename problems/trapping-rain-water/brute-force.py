class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        bucket = {}
        for i in range(len(height)):
            left = i - 1
            leftMostHigh = 0
            while left >= 0:
                leftMostHigh = max(leftMostHigh, height[left])
                left -= 1
            right = i + 1
            rightMostHigh = 0
            while right < len(height):
                rightMostHigh = max(rightMostHigh, height[right])
                right += 1
            
            h = height[i]
            waterTrapped = min(leftMostHigh, rightMostHigh) - h
            currentWaterTrapped = bucket.get(i, 0)
            bucket[i] = max(waterTrapped, currentWaterTrapped)

        totalWaterTrapped = 0
        for k,v in bucket.items():
            print("pos: " + str(k) + " water: " + str(v))
            totalWaterTrapped += v

        return totalWaterTrapped
                
