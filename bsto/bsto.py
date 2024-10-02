# Practices 6&7. Binary Search Tree Operations
import sys
from collections import deque

BUILD = 'B'
FIND_MIN = 'm'
FIND_MAX = 'M'
INSERT = 'I'
DELETE = 'D'
INORDER = 'N'
PREORDER = 'R'
POSTORDER = 'O'


# Node implementation
class TreeNode:
    def __init__(self, k, l=None, r=None):
        self.key = k
        self.left = l
        self.right = r


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Return True if tree is empty; False otherwise
    #  Time Complexity: O(1)
    def isEmpty(self):
        return self.root == None

    # Given a sequence arr of integers, start index l, the end index r,
    # build a binary search (sub)tree that contains keys in arr[l], ..., arr[r].
    # Return the root node of the tree
    #  Time Complexity: O(n) - n: number of elements in the array
    def arrayToBST(self, array, l, r):
        if l > r:
            return None
        # find middle number and fix to root
        mid = (l + r) // 2
        root = TreeNode(array[mid])
        # Recursively traverse the subtree rooted at the child nodes.
        root.left = self.arrayToBST(array, l, mid - 1)
        root.right = self.arrayToBST(array, mid + 1, r)

        return root


    # Move left until there are no more next nodes since the most left node is the smallest node.
    # Time Complexity: O(h) - h: height of the tree
    def findMin(self):
        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return current

    # Return the node with the maximum value
    # Move right until there are no more next nodes since the most right node is the largest node.
    # Time Complexity: O(h) - h: height of the tree
    def findMax(self):
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current


    def _getHeight(self, curr):
        if not curr:
            return 0
        return 1 + max(self._getHeight(curr.left), self._getHeight(curr.right))

    def _printSpaces(self, n, curr):
        for i in range(int(n)):
            print("  ", end="")
        if not curr:
            print(" ", end="")
        else:
            print(str(curr.key), end="")

    def printTree(self):
        if not self.root:
            return
        q = deque()
        q.append(self.root)
        temp = deque()
        cnt = 0
        height = self._getHeight(self.root) - 1
        nMaxNodes = 2 ** (height + 1) - 1
        while cnt <= height:
            curr = q.popleft()
            if len(temp) == 0:
                self._printSpaces(nMaxNodes / (2 ** (cnt + 1)), curr)
            else:
                self._printSpaces(nMaxNodes / (2 ** cnt), curr)
            if not curr:
                temp.append(None)
                temp.append(None)
            else:
                temp.append(curr.left)
                temp.append(curr.right)
            if len(q) == 0:
                print("\n")
                q = temp
                temp = deque()
                cnt += 1

    # Given a query, search for the node whose key is equal to query.
    # If the node exists, return the key
    # Otherwise, return nullptr
    # Time Complexity:The time complexity of this function is O(log n) in the average case,
    # However, in the worst case scenario where the tree is unbalanced,
    # the time complexity could degrade to O(n), where N is the number ofnodes in the tree.
    # This occurs if the tree is a skewed tree

    def search(self, query):
        current = self.root
        while current:
            if current.key is query:
                return current
            elif current.key < query:
                current = current.right
            else:
                current = current.left
        return None

    # Given an output file, write the keys of all the nodes
    # visited in inorder traversal
    # Time Complexity:The time complexity of this function is O(n) in the average case,
    def writeInorder(self, outFile, node):
        if node is not None:
            self.writeInorder(outFile, node.left)
            outFile.write(str(node.key) + " ")
            self.writeInorder(outFile, node.right)

    # Given an output file, write the keys of all the nodes
    # visited in preorder traversal
    # Time Complexity:The time complexity of this function is O(n) in the average case,

    def writePreorder(self, outFile, node):
        if node is not None:
            outFile.write(str(node.key) + " ")
            self.writePreorder(outFile, node.left)
            self.writePreorder(outFile, node.right)

    # Given an output file, write the keys of all the nodes
    # visited in postorder traversal
    # Time Complexity:The time complexity of this function is O(n) in the average case,
    def writePostorder(self, outFile, node):
        if node is not None:
            self.writePostorder(outFile, node.left)
            self.writePostorder(outFile, node.right)
            outFile.write(str(node.key) + " ")

    # If node with key k already exists in the tree, do nothing
    # Otherwise, insert new node with key k
    # Time Complexity : The time complexity of this function is O(log n) in the average case,
    # However, in the worst case scenario where the tree is unbalanced,
    # the time complexity could degrade to O(n), where N is the number ofnodes in the tree.
    # This occurs if the tree is a skewed tree

    def insertNode(self, k):
        self.root = self._insertNode(self.root, k)
    # The _insertNode method recursively inserts a node into
    # the binary search tree by traversing down from the root node
    def _insertNode(self, node, k):
        if node is None:
            node = TreeNode(k)
            return node
        if k == node.key:
            return None
        if k < node.key:
            node.left = self._insertNode(node.left, k)
        else:
            node.right = self._insertNode(node.right, k)
        return node



    # If deletion fails, immediately terminate the program
    # Otherwise, delete the node with key k
    # Time Complexity : time complexity of this method is O(h), where h is the height of the tree.
    def deleteNode(self, k):
        self.root = self._deleteNode(self.root, k)

    def _deleteNode(self, node, k):
        if node is None:
            return None
        if k < node.key:
            node.left = self._deleteNode(node.left, k)
        elif k > node.key:
            node.right = self._deleteNode(node.right, k)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = node.right

            while temp.left is not None:
                temp = temp.left
            node.key = temp.key
            node.right = self._deleteNode(node.right, temp.key)
        return node


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise Exception("Correct usage: [program] [input] [output]")

    tree = BinarySearchTree()
    with open(sys.argv[1], 'r') as inFile:
        lines = inFile.readlines()
    with open(sys.argv[2], 'w') as outFile:
        for line in lines:
            words = line.split()
            op = words[0]
            if op == BUILD:
                data = [int(s) for s in words[1:]]
                tree.root = tree.arrayToBST(data, 0, len(data) - 1)
                if tree.root:
                    outFile.write(BUILD + "\n")
                    tree.printTree()
                else:
                    raise Exception("BUILD: invalid input")
            elif op == FIND_MIN:
                found = tree.findMin()
                if not found:
                    raise Exception("FindMin failed")
                else:
                    outFile.write(str(found.key) + "\n")
            elif op == FIND_MAX:
                found = tree.findMax()
                if not found:
                    raise Exception("FindMax failed")
                else:
                    outFile.write(str(found.key) + "\n")

            elif op == SEARCH:
                if len(words) != 2:
                    raise Exception("SEARCH: invalid input")
                k = int(words[1])
                found = tree.search(k)
                if not found:
                    raise Exception("Search failed")
                else:
                    outFile.write(str(found.key) + "\n")

            elif op == INORDER:
                tree.writeInorder(outFile, tree.root)
                outFile.write("\n")

            elif op == PREORDER:
                tree.writePreorder(outFile, tree.root)
                outFile.write("\n")

            elif op == POSTORDER:
                tree.writePostorder(outFile, tree.root)
                outFile.write("\n")

            elif op == INSERT:
                if len(words) != 2:
                    raise Exception("INSERT: invalid input")
                k = int(words[1])
                if len(words) != 2:
                    raise Exception("INSERT: invalid input")
                k = int(words[1])
                tree.insertNode(k)
            elif op == DELETE:
                if len(words) != 2:
                    raise Exception("DELETE: invalid input")
                k = int(words[1])
                tree.deleteNode(k)
            else:
                raise Exception("Undefined operator")