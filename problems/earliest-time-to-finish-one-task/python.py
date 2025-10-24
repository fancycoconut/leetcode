class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        totalTimeTaken = []
        for task in tasks:
            totalTimeTaken.append(task[0] + task[1])

        earliestTime = totalTimeTaken[0]
        for i in range(1, len(totalTimeTaken)):
            earliestTime = min(earliestTime, totalTimeTaken[i])

        return earliestTime
