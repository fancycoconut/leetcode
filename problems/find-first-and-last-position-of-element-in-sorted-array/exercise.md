# 34. Find First and Last Position of Element in Sorted Array

Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with `O(log n)` runtime complexity.

### Example 1:

```text
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
```

### Example 2:

```text
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```

### Example 3:

```text
Input: nums = [], target = 0
Output: [-1,-1]
```

### Constraints:

- 0 <= nums.length <= 10<sup>5</sup>
- -10<sup>9</sup> <= nums[i] <= 10<sup>9</sup>
- `nums` is a non-decreasing array.
- -10<sup>9</sup> <= target <= 10<sup>9</sup>
