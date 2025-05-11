class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        item = self.map[key]
        self.remove(item)
        self.add(item)
        return item.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            oldNode = self.map[key]
            self.remove(oldNode)
        node = Node(key, value)
        self.map[key] = node
        self.add(node)

        if len(self.map) > self.capacity:
            nodeToDelete = self.head.next
            self.remove(nodeToDelete)
            self.map.pop(nodeToDelete.key, None)

        #self.print()

    def add(self, node: Node) -> None:
        prevTail = self.tail.prev
        prevTail.next = node
        node.prev = prevTail
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node: Node) -> None:
        prev = node.prev
        prev.next = node.next
        node.next.prev = prev

    def print(self) -> None:
        output = []
        current = self.head
        while current is not None:
            output.append(current)
            current = current.next
        print("[" + ",".join(str(x.val) for x in output) + "]")

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)