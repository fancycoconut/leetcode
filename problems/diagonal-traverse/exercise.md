# 498. Diagonal Traverse

Given an `m x n` matrix `mat`, return *an array of all the elements of the array in a diagonal order*.

### Example 1:

![image](diag1-grid.jpg)

```text
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
```

### Example 2:

```text
Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
```

### Constraints:

- `m == mat.length`
- `n == mat[i].length`
- 1 <= m, n <= 10<sup>4</sup>
- 1 <= m * n <= 10<sup>4</sup>
- -10<sup>5</sup> <= mat[i][j] <= 10<sup>5</sup>
