# Practice 5. Binary Search Tree
import sys
from collections import deque

BUILD = 'B'  # 주어진 배열을 이진탐색트리로 변환
FIND_MIN = 'm'  # 트리에서 최소값을 가진 노드를 찾는다
FIND_MAX = 'M'  # 트리에서 최대값을 가진 노드를 찾는다.


# Node implementation
class TreeNode:
    # Properties include left child node (left), right child node (right)
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):  # Automatically called when object is created (Constructor)
        self.root = None

        # Return True if tree is empty; False otherwise

    def isEmpty(self):
        # TODO
        if self.root == None:
            return True
        else:
            return False

    # Given a sequence arr of integers, start index l, the end index r,
    # build a binary search (sub)tree that contains keys in arr[l], ..., arr[r].
    # Return the root node of the tree
    def arrayToBST(self, arr, l, r):  # Convert given array to binary search tree
        # TODO
        if l > r:
            return None
        for i in range(len(arr) - 1):  # O(n)
            if arr[i] > arr[i + 1]:
                return None
        # make the middle element the root
        mid = (l + r) // 2
        root = TreeNode(arr[mid])  # node 객체 생성, key = arr[mid]
        # Use of recursive functions
        # Use your own different methods within the class
        root.left = self.arrayToBST(arr, l, mid - 1)  # O(logn)
        root.right = self.arrayToBST(arr, mid + 1, r)  # O(logn)
        return root

    # Return the node with the minimum value
    def findMin(self):
        # TODO
        if self.root == None:  # O(logn)
            return None

        current = self.root
        while current.left != None:  # O(logn)
            current = current.left

        return current

    # Return the node with the maximum value
    def findMax(self):
        # TODO
        if self.root == None:
            return None
        current = self.root
        while current.right != None:  # O(logn)
            current = current.right
        return current

    def _getHeight(self, curr):  # O(n)
        if not curr:
            return 0
        return 1 + max(self._getHeight(curr.left), self._getHeight(curr.right))  # O(n)

    def _printSpaces(self, n, curr):
        for i in range(int(n)):
            print("  ", end="")
        if not curr:
            print(" ", end="")
        else:
            print(str(curr.key), end="")

    def printTree(self):  # O(n)
        if not self.root:
            return
        q = deque()
        q.append(self.root)
        temp = deque()
        cnt = 0
        height = self._getHeight(self.root) - 1  # O(n)
        nMaxNodes = 2 ** (height + 1) - 1
        while cnt <= height:  # O(n)
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
            else:
                raise Exception("Undefined operator")

