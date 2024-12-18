public class Solution {
    public int[] TwoSum(int[] numbers, int target) {
        var pointer1 = 0;
        var pointer2 = numbers.Length - 1;

        while (pointer1 < pointer2)
        {
            var sum = numbers[pointer1] + numbers[pointer2];
            if (sum == target)
            {
                return [pointer1 + 1, pointer2 + 1];
            }

            //Console.WriteLine(sum);

            if (sum < target)
            {
                pointer1++;
            }
            else
            {
                pointer2--;
            }
        }

        return [];
    }
}