from typing import Dict


class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.is_end_of_word: bool = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_end_of_word = True

    def search(self, word: str) -> bool:
        def searchHelper(node: TrieNode, word: str) -> bool:
            current_node = node
            for index, char in enumerate(word):
                if char == ".":
                    """
                    There is chance that '.' is the last char but current_node doesn't have any child
                    So following code will be problematic

                    if index == len(word) - 1:
                        return True

                    If the the current_nodes doesn't have any child it will be evaluated as true,
                    but the last '.' doesn't have any character to be mapped too
                    """
                    return any(
                        (index == len(word) - 1 and sub_nodes.is_end_of_word)
                        or searchHelper(sub_nodes, word[index + 1 :])
                        for sub_nodes in current_node.children.values()
                    )
                if char in current_node.children:
                    current_node = current_node.children[char]
                else:
                    return False
            return current_node.is_end_of_word

        return searchHelper(self.root, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
