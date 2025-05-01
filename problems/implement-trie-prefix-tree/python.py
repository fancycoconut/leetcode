class Trie:

    def __init__(self):
        self.children = {}
        self.words = set()

    def insert(self, word: str) -> None:
        root = self
        current = root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = Trie()
            current = current.children[letter]      
                
        self.words.add(word)
        
    def search(self, word: str) -> bool:
        return word in self.words

    def startsWith(self, prefix: str) -> bool:
        root = self
        current = root
        for letter in prefix:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return True    


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)