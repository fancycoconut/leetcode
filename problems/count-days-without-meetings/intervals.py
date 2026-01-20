class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetingDays = sorted(meetings, key=lambda int:int[0])

        mergedMeetingDays = []
        current = meetingDays[0]
        for i in range(1, len(meetingDays)):
            interval = meetingDays[i]

            if interval[0] > current[1]:
                mergedMeetingDays.append(current)
                current = interval
            else:
                start = current[0]
                end = max(current[1], interval[1])
                current = (start, end)
        mergedMeetingDays.append(current)

        totalMeetingDays = 0
        for meeting in mergedMeetingDays:
            totalMeetingDays += (meeting[1] - meeting[0]) + 1
        #print(totalMeetingDays)

        return days - totalMeetingDays
