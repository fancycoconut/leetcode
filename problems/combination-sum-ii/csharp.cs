public class Solution {
    public IList<IList<int>> CombinationSum2(int[] candidates, int target) {
        var results = new List<IList<int>>();
        var combinations = new List<int>();

        Array.Sort(candidates);

        Backtrack(0, 0, target, candidates, combinations, results);

        return results.ToList();
    }

    private void Backtrack(int start, int currentSum, int target, int[] candidates, List<int> combinations, List<IList<int>> results)
    {
        if (currentSum > target) return;
        if (currentSum == target)
        {
            results.Add(new List<int>(combinations));
            return;
        }

        for (var i = start; i < candidates.Length; i++)
        {
            if (i > start && candidates[i] == candidates[i-1]) continue;
            combinations.Add(candidates[i]);

            Backtrack(i + 1, currentSum + candidates[i], target, candidates, combinations, results);

            combinations.RemoveAt(combinations.Count - 1);
        }
    }
}