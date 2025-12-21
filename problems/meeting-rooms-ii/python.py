class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        startIntervals = sorted(interval[0] for interval in intervals)
        endIntervals = sorted(interval[1] for interval in intervals)
        
        res, count = 0, 0
        i, j = 0, 0
        while i < len(startIntervals):
            # check the start time against the end time to see if there is a meeting already in progress
            # if there is then a new room is needed otherwise we can reuse the same room
            if startIntervals[i] < endIntervals[j]:
                i += 1
                count += 1
            else:
                j += 1
                count -= 1
            res = max(count, res)

        return res
