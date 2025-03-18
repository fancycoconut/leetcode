class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left = 0
        right = len(intervals)

        # Use binary search to find position to insert
        while left < right:
            mid = (left + right) // 2

            if intervals[mid][0] < newInterval[0]:
                left = mid + 1
            else:
                right = mid
        intervals.insert(left, newInterval)

        # Merge all
        current = intervals[0]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            start = interval[0]
            end = interval[1]

            if current[1] >= start:
                current[1] = max(current[1], end)
                interval[0] = -1
                interval[1] = -1
                continue

            current = interval
        #print(intervals)

        output = []
        for interval in intervals:
            if interval[0] == -1 and interval[1] == -1:
                continue

            output.append(interval)

        return output
