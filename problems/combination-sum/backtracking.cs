public class Solution {
    public IList<IList<int>> CombinationSum(int[] candidates, int target) {
        var results = new List<IList<int>>();
        var combinations = new List<int>();

        FindCombinationSum(0, target, candidates, combinations, results);

        return results;
    }

    private void FindCombinationSum(int start, int remaining, int[] candidates, List<int> combinations, List<IList<int>> results)
    {
        if (remaining == 0) {
            results.Add(new List<int>(combinations));
            return;
        }
        if (remaining < 0) return;

        for (var i = start; i < candidates.Length; i++)
        {
            combinations.Add(candidates[i]);

            FindCombinationSum(i, remaining - candidates[i], candidates, combinations, results);

            combinations.RemoveAt(combinations.Count - 1);
        }
    }
}