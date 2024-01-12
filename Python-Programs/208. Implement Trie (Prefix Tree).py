class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}
        self.isEndOfWord = False
        

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        current = self
        for i in word:
            if i not in current.children:
                current.children[i] = Trie()
            current = current.children[i]
        current.isEndOfWord = True

        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        current = self
        for i in word:
            if i not in current.children:
                return False
            current = current.children[i]
        return current.isEndOfWord
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        current = self
        for i in prefix:
            if i not in current.children:
                return False
            current = current.children[i]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)