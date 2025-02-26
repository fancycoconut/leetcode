class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.swap(0, s)
        
    def swap(self, index: int, s: List[str]):
        mid = math.floor(len(s) / 2)
        if index >= mid:
            return
        first = index
        last = len(s) - index - 1
        
        temp = s[last]
        s[last] = s[first]
        s[first] = temp
        self.swap(index + 1, s)
        