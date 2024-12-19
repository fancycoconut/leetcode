// Using 2 pointers approach
public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        var indexMap = BuildIndexMap(nums);

        var start = 0;
        var end = nums.Length - 1;

        Array.Sort(nums);

        var output = new HashSet<int>();
        while (start < nums.Length && start != end && end >= 0)
        {
            var left = nums[start];
            var right = nums[end];
            var sum = left + right;
            if (sum == target)
            {
                indexMap[left].ForEach(x => output.Add(x));
                indexMap[right].ForEach(x => output.Add(x));
                break;
            }
            if (sum > target)
            {
                end--;
                continue;
            }

            start++;
        }

        return output.ToArray();
    }

    private Dictionary<int, List<int>> BuildIndexMap(int[] nums)
    {
        var indexMap = new Dictionary<int, List<int>>();
        for (var i = 0; i < nums.Length; i++)
        {
            var num = nums[i];
            if (indexMap.ContainsKey(num))
            {
                indexMap[num].Add(i);
            }
            else
            {
                indexMap[num] = new List<int> { i };
            }            
        }
        return indexMap;
    }
}