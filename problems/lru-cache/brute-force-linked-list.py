class ListNode:
    def __init__(self, key: int, val: int, age: int = 0):
        self.key = key
        self.val = val
        self.age = age
        self.next = None

class LRUCache:
    capacity = 0
    maxCapacity = 0
    cacheItemRoot = None
    newestAge = 0

    def __init__(self, capacity: int):
        self.maxCapacity = capacity

    def get(self, key: int) -> int:
        item = self.findItem(key)
        if item is None:
            return -1
        self.newestAge += 1
        item.age = self.newestAge
        return item.val

    def put(self, key: int, value: int) -> None:
        item = self.findItem(key)
        self.newestAge += 1
        
        if item is None:
            if self.capacity == 0:
                self.cacheItemRoot = ListNode(key, value, self.newestAge)
                self.capacity += 1
                #self.print()
                return
            if self.capacity == self.maxCapacity:
                oldestItem = self.findOldestItem()
                oldestItem.key = key
                oldestItem.val = value
                oldestItem.age = self.newestAge
                #self.print()
                return
            newItem = ListNode(key, value, self.newestAge)
            item = self.cacheItemRoot
            while item.next is not None:
                item = item.next
            item.next = newItem
            self.capacity += 1
            #self.print()
        else:
            item.val = value
            item.age = self.newestAge

    def findItem(self, key: int) -> ListNode:
        item = self.cacheItemRoot
        while item is not None:
            if item.key == key:
                return item
            item = item.next
        return None

    def findNewestItem(self) -> ListNode:
        maxAge = 0
        newestItem = None
        item = self.cacheItemRoot
        while item is not None:
            if item.age > maxAge:
                maxAge = item.age
                newestItem = item
            item = item.next
        return newestItem

    def findOldestItem(self) -> ListNode:
        age = float('inf')
        oldestItem = None
        item = self.cacheItemRoot
        while item is not None:
            if item.age < age:
                age = item.age
                oldestItem = item
            item = item.next
        return oldestItem

    def print(self) -> None:
        items = []
        item = self.cacheItemRoot
        while item is not None:
            items.append(item.val)
            item = item.next
        print("[" + ",".join(str(x) for x in items) + str("]"))


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)