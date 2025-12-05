class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        intervals.sort(key=lambda tup: tup[0])

        working_interval = intervals[0]

        i = 1
        while i < len(intervals):
            interval = intervals[i]

            # Cannot merge so insert
            if interval[0] > working_interval[1]:
                output.append(working_interval)
                working_interval = interval
            else:
                start = working_interval[0]
                end = max(working_interval[1], interval[1])
                working_interval = (start, end)
            i += 1
        output.append(working_interval)
        #print(output)

        return output
