public class Solution {
    public IList<IList<int>> ThreeSum(int[] nums) {
        Array.Sort(nums);

        var triplets = new HashSet<(int, int, int)>();
        for (var i = 0; i < nums.Length; i++)
        {
            var target = nums[i] >= 0
                ? nums[i] * -1
                : Math.Abs(nums[i]);

            var results = TwoSum(nums[(i+1)..], target);
            foreach (var result in results)
            {
                //Console.WriteLine($"Result: ({result.Item1}, {result.Item2})");
                var sum = nums[i] + result.Item1 + result.Item2;
                if (sum != 0) continue;
                var temp = new int[] { nums[i], result.Item1, result.Item2 };
                Array.Sort(temp);
                triplets.Add((temp[0], temp[1], temp[2]));
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

    private List<(int, int)> TwoSum(int[] sums, int target)
    {
        var output = new HashSet<(int, int)>();

        var left = 0;
        var right = sums.Length - 1;
        while (left < sums.Length && right >= 0 && left != right)
        {
            var sum = sums[left] + sums[right];
            if (sum == target)
            {
                output.Add((sums[left], sums[right]));
                left++;
                right--;
                continue;
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

        return output.ToList();
    }
}