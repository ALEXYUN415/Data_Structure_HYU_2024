# Practice 9. Max Heap
import sys

INSERT = 'I'
DELETE = 'D'
MAXIMUM = 'M'
MAX_CAPACITY = 1000
INT_MIN = -sys.maxsize


class MaxHeap:
    def __init__(self, num=MAX_CAPACITY):
        self.elements = [0] * num
        self.count = 0
        self.capacity = num

    # Given the index i of element, return the index of that element's parent in the heap
    def parent(self, i):
        return (i - 1) // 2

    # Given the index i of element, return the index of that element's left child in the heap
    def left(self, i):
        return 2 * i + 1

    # Given the index i of element, return the index of that element's right child in the heap
    def right(self, i):
        return 2 * i + 2

    # Insert a given element elem into the heap
    # If the insertion fails, immediately terminate the program with the error message.
    def insertElement(self, elem):
        if self.count == self.capacity:
            raise Exception("insertion error")
        else:
            self.count += 1
            i = self.count - 1
            self.elements[i] = elem
            while i != 0 and self.elements[self.parent(i)] < self.elements[i]:
                self.elements[i], self.elements[self.parent(i)] = self.elements[self.parent(i)], self.elements[i]
                i = self.parent(i)
                # 파이썬의 바로 교환가능한 엄청난 기능 사용....

    # Return the maximum of the heap if it exists
    # Otherwise, terminate program with an error
    def maximum(self):
        if self.count == 0:
            raise Exception("Error")
        return self.elements[0]


    # Delete the maximum from the heap and return the maximum
    # If deletion fails, terminate program with an error
    def deleteMaximum(self):
        if self.count == 0:
            raise Exception("Error")
        if self.count == 1:
            self.count -= 1
            return self.elements[0]

        root = self.elements[0]
        self.elements[0] = self.elements[self.count - 1]
        self.count -= 1
        self.maxHeapify(0)
        return root

    def maxHeapify(self, i):
        left_child = self.left(i)
        right_child = self.right(i)
        largest = i

        if left_child < self.count and self.elements[i] < self.elements[left_child]:
            largest = left_child

        if right_child < self.count and self.elements[i] < self.elements[right_child]:
            largest = right_child
        if largest != i:
            self.elements[i], self.elements[largest] = self.elements[largest], self.elements[i]
            self.maxHeapify(largest)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise Exception("Correct usage: [program] [input] [output]")

    h = MaxHeap()
    with open(sys.argv[1], 'r') as inFile:
        lines = inFile.readlines()
    with open(sys.argv[2], 'w') as outFile:
        for line in lines:
            words = line.split()
            op = words[0]
            if op == INSERT:
                if len(words) != 2:
                    raise Exception("INSERT: invalid input")
                i = int(words[1])
                h.insertElement(i)
                for element in h.elements[:h.count]:
                    outFile.write(str(element) + " ")
                outFile.write("\n")
            elif op == DELETE:
                deleted_max = h.deleteMaximum()
                for element in h.elements[:h.count]:
                    outFile.write(str(element) + " ")
                outFile.write("\n")
            elif op == MAXIMUM:
                maximum = h.maximum()
                outFile.write(str(maximum) + "\n")
            else:
                raise Exception("Undefined operator")



