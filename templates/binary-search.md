# Binary Search

Complexity: O log N

## General Technique

### Python

```python
def binarySearch(nums: List[int], target: int) -> int
  left = 0
  right = len(nums)

  while left < right:
    mid = (left + right) // 2

    if nums[mid] < target:
      left = mid + 1
    else:
      right = mid
  return left
```

### C#

```c#
int BinarySearch(int[] nums)
{
  var left = 0;
  var right = nums.Length;

  while (left < right)
  {
    var mid = (left + right) / 2;
    if (nums[mid] < target)
      left = mid + 1
    else
      right = mid
  }

  return left
}
```

### Rotated Sorted Arrays

For rotated sorted arrays, we just need to find the pivot / inflection point. This is always the smallest element.

```python
def findPivotPoint(nums: List[int]) -> int
  left = 0
  right = len(nums) - 1

  # Find pivot point ie. smallest element in rotated array
  while left <= right:
    mid = (left + right) // 2

    if nums[mid] > nums[-1]:
      left = mid + 1
    else:
      right = mid - 1
  return left
```
