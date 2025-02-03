/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

public class Solution : GuessGame {
    public int GuessNumber(int n) {
        var low = 1;
        var high = n;
        while (low <= high)
        {
            var mid = low + (high - low) / 2;
            var res = guess(mid);
            if (res == 0) return mid;
            if (res == -1)
            {
                high = mid - 1;
                continue;
            }

            low = mid + 1;
        }

        return -1;
    }
}