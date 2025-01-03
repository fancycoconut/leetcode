// Solution using backtracking
public class Solution {
    public IList<IList<int>> Subsets(int[] nums) {
        var result = new List<IList<int>>();

        Backtrack(0, nums, new List<int>(), result);

        return result;
    }

    private void Backtrack(int start, int[] nums, List<int> subset, List<IList<int>> results)
    {
        results.Add(new List<int>(subset));

        for (var i = start; i < nums.Length; i++)
        {
            subset.Add(nums[i]);

            Backtrack(i + 1, nums, subset, results);

            // Remove last element
            subset.RemoveAt(subset.Count - 1);
        }
    }
}