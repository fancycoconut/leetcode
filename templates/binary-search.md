# Binary Search

Complexity: O log N

## Python

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

## C#

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
