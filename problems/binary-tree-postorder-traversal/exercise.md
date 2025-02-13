# 145. Binary Tree Postorder Traversal

Given the `root` of a binary tree, return *the postorder traversal of its nodes' values*.

### Example 1:

```text
Input: root = [1,null,2,3]

Output: [3,2,1]

Explanation:

```

![image](screenshot-2024-08-29-202743.png)

### Example 2:

```text
Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [4,6,7,5,2,9,8,3,1]

Explanation:
```

![image](tree_2.png)

### Example 3:

```text
Input: root = []

Output: []
```

### Example 4:

```text
Input: root = [1]

Output: [1]
```

### Constraints:

- The number of the nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

**Follow up:** Recursive solution is trivial, could you do it iteratively?
