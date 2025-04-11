# Monotonic Queue

```python
# Monotonic Queue(Decreasing)
from collections import deque

class MonotonicQueue:
    def __init__(self):
        self.q = deque()

    def push(self, value):
        # Remove all elements smaller than the current value
        while self.q and self.q[-1] < value:
            self.q.pop()
        self.q.append(value)

    def pop(self, value):
        # Only pop from front if it's equal to the value to remove
        if self.q and self.q[0] == value:
            self.q.popleft()

    def max(self):
        # The maximum is always at the front
        return self.q[0]
```
