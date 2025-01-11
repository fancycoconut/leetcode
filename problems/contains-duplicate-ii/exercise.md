# 219. Contains Duplicate II

Given an integer array `nums` and an integer `k`, return `true` *if there are two **distinct indices*** `i` *and* `j` *in the array such that* `nums[i] == nums[j]` *and* `abs(i - j) <= k`.

### Example 1:

```text
Input: nums = [1,2,3,1], k = 3
Output: true
```

### Example 2:

```text
Input: nums = [1,0,1,1], k = 1
Output: true
```

### Example 3:

```text
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
``` 

### Constraints:

- 1 <= nums.length <= 10<sup>5</sup>
- -10<sup>9</sup> <= nums[i] <= 10<sup>9</sup>
- 0 <= k <= 10<sup>5</sup>
