class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) == 0:
            return True
        intervals.sort(key= lambda tup: tup[0])
        wi = intervals[0]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] >= wi[1]:
                wi = interval
            else:
                return False

        return True