public class Solution {
    public int[][] Merge(int[][] intervals) {
        // TODO sort by start time
        Array.Sort(intervals, new IntervalComparer());

        var workingInterval = intervals[0];
        for (var i = 1; i < intervals.Length; i++)
        {
            var currentInterval = intervals[i];
            var workingIntervalEnd = workingInterval[1];
            var currentIntervalStart = currentInterval[0];

            // Can be merged?
            if (workingIntervalEnd >= currentIntervalStart)
            {
                workingInterval[1] = Math.Max(currentInterval[1], workingInterval[1]);
                currentInterval[0] = -1;
                currentInterval[1] = -1;
                continue;
            }

            workingInterval = currentInterval;
        }

        var results = new List<int[]>();
        foreach (var interval in intervals)
        {
            if (interval[0] == -1 && interval[1] == -1) continue;
            results.Add(interval);
        }

        return results.ToArray();
    }

    private class IntervalComparer : IComparer<int[]>
    {
        public int Compare(int[] x, int[] y)
        {
            if (x[0].CompareTo(y[0]) != 0) return x[0].CompareTo(y[0]);
            return 0;
        }
    }
}