import sys
BUILD_TRIE = 'T'
AUTOCOMPLETE = 'A'
ENDS_HERE = '#'
#practice 15

class Trie_Node:
    def __init__(self):
        self.child = {}
        self.endWord = False

class Trie:
    def __init__(self):
        self.root = Trie_Node()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.child:
                node.child[char] = Trie_Node()
            node = node.child[char]
        node.endWord = True

    def search(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.child:
                return []
            node = node.child[char]
        return self.autocomplete(node, prefix)

    def autocomplete(self, node, prefix):
        results = []
        if node.endWord:
            results.append(prefix)
        for char, next_node in node.child.items():
            results.extend(self.autocomplete(next_node, prefix + char))
        return results


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise Exception("Correct usage: [program] [input] [output]")

    with open(sys.argv[1], 'r') as inFile:
        lines = inFile.readlines()

    with open(sys.argv[2], 'w') as outFile:
        i = 0
        trie = Trie()

        while i < len(lines):
            words = lines[i].split()
            op = words[0]
            if op == BUILD_TRIE:
                if len(words) != 2:
                    raise Exception("BUILD_TRIE: invalid input")
                n = int(words[1])
                strings = []
                while n:
                    i = i + 1
                    strings.append(lines[i].strip())
                    n = n - 1
                for string in strings:
                    trie.insert(string)

            elif op == AUTOCOMPLETE:
                if len(words) != 2:
                    raise Exception("AUTOCOMPLETE: invalid input")
                prefix = words[1]
                results = trie.search(prefix)
                for out in results:
                    outFile.write(out + " ")
                outFile.write("\n")
            else:
                raise Exception("Undefined operator")
            i = i + 1