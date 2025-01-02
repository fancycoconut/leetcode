public class Solution {
    public IList<IList<int>> ThreeSum(int[] nums) {
        Array.Sort(nums);

        var triplets = new HashSet<(int, int, int)>();
        for (var i = 0; i < nums.Length; i++)
        {
            var num = nums[i];
            var target = num >= 0
                ? num * -1
                : Math.Abs(num);

            var twoSumResults = TwoSum(nums[(i+1)..], target);
            
            var result = num + twoSumResults.Item1 + twoSumResults.Item2;
            if (result == 0)
            {
                triplets.Add((num, twoSumResults.Item1, twoSumResults.Item2));
                continue;
            }
        }

        var output = new List<IList<int>>();

        foreach (var triplet in triplets)
        {
            var tripletList = new List<int>();
            tripletList.Add(triplet.Item1);
            tripletList.Add(triplet.Item2);
            tripletList.Add(triplet.Item3);
            output.Add(tripletList);
        }

        return output;
    }

    private (int, int) TwoSum(int[] sums, int target)
    {
        //var output = new List<(int, int)>();

        var left = 0;
        var right = sums.Length - 1;
        while (left < sums.Length && right >= 0 && left != right)
        {
            var sum = sums[left] + sums[right];
            if (sum == target)
            {
                return (sums[left], sums[right]);
            }

            if (sum < target)
            {
                left++;
            }
            else
            {
                right--;
            }
        }

        return (255, 255);
    }
}