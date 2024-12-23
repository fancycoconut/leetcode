public class Solution {
    public int RemoveElement(int[] nums, int val) {
        var start = 0;
        var end = nums.Length - 1;

        while (start < nums.Length && end >= 0 && start != end)
        {
            var num = nums[start];
            var endNum = nums[end];
            if (endNum == val)
            {
                end--;
                continue;
            }

            if (num == val)
            {
                var temp = nums[end];
                nums[end] = nums[start];
                nums[start] = temp;
                end--;
                continue;
            }

            start++;
        }

        var numOfElementsRemoved = 0;
        for (var i = 0; i < nums.Length; i++)
        {
            var num = nums[i];
            if (num == val) break;
            numOfElementsRemoved++;
        }
        
        return numOfElementsRemoved;
    }
}