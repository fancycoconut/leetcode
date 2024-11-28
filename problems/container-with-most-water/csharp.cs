public class Solution {
    public int MaxArea(int[] height) {
        var maxArea = 0;

        var left = 0;
        var right = height.Length - 1;
        while (left != right && left < height.Length && right > 0)
        {
            var rightIsTaller = height[right] > height[left];

            var h = rightIsTaller ? height[left] : height[right];
            var w = right - left;
            var area = h * w;
            Console.WriteLine($"Area: {area}");
            maxArea = Math.Max(maxArea, area);

            if (rightIsTaller)
                left++;
            else
                right--;
        }

        return maxArea;
    }
}