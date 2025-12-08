# Sorting

## Merge Sort

Complexity: O (n log n)

```python
def mergeSort(nums: list[int]) -> list[int]:
  n = len(nums)
  if n == 0 or n == 1:
    return nums

  mid = n // 2
  left = mergeSort(nums[:mid])
  right = mergeSort(nums[mid:])

  return merge(left, right)

def merge(left: list[int], right: list[int]) -> list[int]:
  output = []

  i = 0
  j = 0
  while i < len(left) and j < len(right):
    a = left[i]
    b = right[j]

    if a < b:
      output.append(a)
      i += 1
    else:
      output.append(b)
      j += 1

    while i < len(left):
      output.append(left[i])
      i += 1

    while j < len(right):
      output.append(right[j])
      j += 1

  return output
```
