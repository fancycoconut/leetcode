# 875. Koko Eating Bananas

Koko loves to eat bananas. There are `n` piles of bananas, the `ith` pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return *the minimum integer* `k` *such that she can eat all the bananas within* `h` *hours*.

### Example 1:

```text
Input: piles = [1,4,3,2], h = 9
Output: 2

Explanation: With an eating rate of 2, you can eat the bananas in 6 hours. With an eating rate of 1, you would need 10 hours to eat all the bananas (which exceeds h=9), thus the minimum eating rate is 2.
```

### Example 2:

```text
Input: piles = [3,6,7,11], h = 8
Output: 4
```

### Example 3:

```text
Input: piles = [30,11,23,4,20], h = 5
Output: 30
```

### Example 4:

```text
Input: piles = [30,11,23,4,20], h = 6
Output: 23
```

### Constraints:

- `1 <= piles.length <= 104`
- `piles.length <= h <= 109`
- `1 <= piles[i] <= 109`
