BUILD = 'B'
FIND_MIN = 'm'
FIND_MAX = 'M'

import sys
from collections import deque


# Node implementation
class TreeNode:
    def __init__(self, ds):
        self.ds = ds
        self.left = None
        self.right = None

# Initializes an empty binary search tree.
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Return True if tree is empty; False otherwise
    #  Time Complexity: O(1)
    def isEmpty(self):
        if self.root.left == None and self.root.right == None:
            return True
        else:
            return False

    # Given a sequence arr of integers, start index l, the end index r,
    # build a binary search (sub)tree that contains keys in arr[l], ..., arr[r].
    # Return the root node of the tree
    #  Time Complexity: O(n) - n: number of elements in the array
    def arrayToBST(self, array, left, right):
        if left > right:
            return None
        # find middle number and fix to root
        mid = (left + right) // 2
        root = TreeNode(array[mid])
        # Recursively traverse the subtree rooted at the child nodes.
        root.left = self.arrayToBST(array, left, mid - 1)
        root.right = self.arrayToBST(array, mid + 1, right)

        return root

    # Return the node with the minimum value
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


    # Time Complexity: O(n) - n: number of nodes in the subtree rooted at the given node
    def _getHeight(self, curr):
        if not curr:
            return 0
        return 1 + max(self._getHeight(curr.left), self._getHeight(curr.right))

    # Time Complexity: O(n) - n: number of nodes in the subtree rooted at the given node
    def _printSpaces(self, n, curnode):
        for i in range(int(n)):
            print("  ", end="")
        if not curnode:
            print("  ", end="")
        else:
            print(str(curnode.ds), end="")

    #  Time Complexity: O(n) - n: number of elements in the array
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
            # I change this part,
            # because the existing code does not work normally when an unsorted numbers are entered
            if op == BUILD:
                data = [int(s) for s in words[1:]]
                if data != sorted(data):
                    raise Exception("BUILD: invalid input")
                tree.root = tree.arrayToBST(data, 0, len(data) - 1)
                if tree.root:
                    outFile.write(BUILD + "\n")
                    tree.printTree()

            elif op == FIND_MIN:
                found = tree.findMin()
                if not found:
                    raise Exception("FindMin failed")
                else:
                    outFile.write(str(found.ds) + "\n")
            elif op == FIND_MAX:
                found = tree.findMax()
                if not found:
                    raise Exception("FindMax failed")
                else:
                    outFile.write(str(found.ds) + "\n")
            else:
                raise Exception("Undefined operator")

