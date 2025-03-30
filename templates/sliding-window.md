# Sliding Window

Complexity: O (N)

### Java

```java
int left = 0, right = 0;

while (right < nums.size()) {
    // expand the window
    window.addLast(nums[right]);
    right++;
    
    while (window needs shrink) {
        // shrink the window
        window.removeFirst(nums[left]);
        left++;
    }
}
```
