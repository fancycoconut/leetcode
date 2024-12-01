public class Solution {
    public bool CheckIfExist(int[] arr) {
        var map = new Dictionary<int, int>();

        foreach (var num in arr)
        {
            if (map.ContainsKey(num))
                map[num]++;
            else
                map.Add(num, 1);
        }

        foreach (var num in arr)
        {
            if (num == 0 && map[0] < 2) {
                continue;
            }

            var @double = num * 2;
            if (map.ContainsKey(@double)) {
                //Console.WriteLine(num);
                return true;
            }
        }

        return false;
    }
}