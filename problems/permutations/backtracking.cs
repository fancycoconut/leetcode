public class Solution {
    public IList<IList<int>> Permute(int[] nums) {
        var results = new List<IList<int>>();
        var subset = new List<int>();

        Backtrack(nums, subset, results);

        return results;
    }

    private void Backtrack(int[] nums, List<int> subset, List<IList<int>> results)
    {
        if (subset.Count == nums.Length)
        {
            results.Add(new List<int>(subset));
            return;
        }

        for (var i = 0; i < nums.Length; i++)
        {
            var num = nums[i];
            if (subset.Contains(num)) continue;
            
            subset.Add(num);

            Backtrack(nums, subset, results);

            subset.RemoveAt(subset.Count - 1);
        }
    }
}