class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        availableTimes1 = sorted(slots1, key=lambda interval: interval[0])
        availableTimes2 = sorted(slots2, key=lambda interval: interval[0])

        i, j = 0, 0
        while i < len(availableTimes1) and j < len(availableTimes2):
            int1 = availableTimes1[i]
            int2 = availableTimes2[j]

            # Get intersection
            start = max(int1[0], int2[0])
            stop = min(int1[1], int2[1])

            # Check if intersection is large enough
            if stop - start >= duration:
                return [ start, start + duration ]

            if int1[1] < int2[1]:
                i += 1
            else:
                j += 1
        return []
