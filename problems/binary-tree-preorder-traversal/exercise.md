# 144. Binary Tree Preorder Traversal

Given the `root` of a binary tree, return *the preorder traversal of its nodes' values*.

### Example 1:

```text
Input: root = [1,null,2,3]

Output: [1,2,3]

Explanation:
```

![image](screenshot-2024-08-29-202743.png)

### Example 2:

```text
Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [1,2,4,5,6,7,3,8,9]

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

- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

**Follow up**: Recursive solution is trivial, could you do it iteratively?
