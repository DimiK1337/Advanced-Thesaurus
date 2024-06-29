import nltk
from nltk.corpus import wordnet as wn

nltk.download('wordnet')
nltk.download('omw-1.4')

class TreeNode:
    def __init__(self, word, depth=0):
        self.word = word
        self.children = []
        self.depth = depth

    def add_child(self, child_node):
        self.children.append(child_node)

class Tree:
    def __init__(self, root_word):
        self.root = TreeNode(root_word)
        self.memo = {}

    def get_synonyms(self, word):
        if word in self.memo:
            return self.memo[word]
        synonyms = set()
        for syn in wn.synsets(word):
            for lemma in syn.lemmas():
                synonyms.add(lemma.name())
        self.memo[word] = synonyms
        return synonyms

    def build_tree(self, node, depth=0, max_depth=2, visited=None):
        if visited is None:
            visited = set()
        if depth > max_depth or node.word in visited:
            return
        visited.add(node.word)
        synonyms = self.get_synonyms(node.word)
        for synonym in synonyms:
            if synonym not in visited:
                child_node = TreeNode(synonym, depth + 1)
                node.add_child(child_node)
                self.build_tree(child_node, depth + 1, max_depth, visited)

    def print_tree(self, node, prefix='', is_last=True):
        connector = '└── ' if is_last else '├── '
        print(f"{prefix}{connector}{node.word} (Depth: {node.depth})")
        prefix += '    ' if is_last else '│   '
        for i, child in enumerate(node.children):
            self.print_tree(child, prefix, i == len(node.children) - 1)

    def visualize_tree(self):
        self.print_tree(self.root)

if __name__ == '__main__':
    input_word = input("Enter a word: ")
    tree = Tree(input_word)
    tree.build_tree(tree.root, max_depth=2)
    tree.visualize_tree()
