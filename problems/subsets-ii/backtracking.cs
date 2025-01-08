public class Solution {
    public IList<IList<int>> SubsetsWithDup(int[] nums) {
        var subset = new List<int>();
        var results = new List<IList<int>>();

        Backtrack(0, nums, subset, results);

        return results;
    }

    private void Backtrack(int start, int[] nums, List<int> subset, List<IList<int>> results)
    {
        results.Add(new List<int>(subset));

        for (var i = start; i < nums.Length; i++)
        {
            if (start != i && nums[i] == nums[i-1]) continue;
            var num = nums[i];

            subset.Add(num);

            Backtrack(i + 1, nums, subset, results);  

            subset.RemoveAt(subset.Count - 1);
        }
    }
}