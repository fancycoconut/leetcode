# 215. Kth Largest Element in an Array

Given an integer array `nums` and an integer `k`, return the k<sup>th</sup> largest element in the array.

Note that it is the k<sup>th</sup> largest element in the sorted order, not the k<sup>th</sup> distinct element.

Can you solve it without sorting?

### Example 1:

```text
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```

### Example 2:

```text
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```

### Constraints:

- 1 <= k <= nums.length <= 10<sup>5</sup>
- -10<sup>4</sup> <= nums[i] <= 10<sup>4</sup>
