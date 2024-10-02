import sys

ADD = 'A'
DELETE = 'D'
FIND = 'F'


class Student:
    def __init__(self, i, n, p=None):
        self.id = i
        self.name = n
        self.next = p

class Course:
    def __init__(self, l=[]):
        if not l:
            self.head = None
            self.size = 0
        else:
            self.head = Node(l[0])
            self.size = len(l)
            curr = self.head
            for x in l[1:]:
                curr.next = Node(x)
                curr = curr.next

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def addStudent(self, newID, newName):
        if self.isEmpty(): # 노드가 없을 때
            self.head = Student(newID, newName)
            self.size += 1
            return True
        if newID < self.head.id:#첫번째 노드로 삽입
            temp = self.head
            self.head = Student(newID, newName, temp)
            self.size += 1
            return True
        else:
            prev = self.head
            curr = self.head
            while curr:
                if curr.id == newID:
                    return False
                if(prev.id < newID) and (newID < curr.id):
                    #현재 노드의 이전 노드가 없거나(not prev) 이전 노드의 ID가 새로운 ID보다 작은 경우에 참.
                    newNode = Student(newID, newName, curr)
                    #Add a node in the middle
                    prev.next = newNode
                    self.size += 1
                    return True
                prev = curr
                curr = curr.next
            #Add a node at the end
            prev.next = Student(newID, newName)
            self.size += 1
            return True

    def deleteStudent(self, queryID):
        if self.head is None:
            print("DELETE: no element exists")
            return False

        curr = self.head
        prev = None

        while curr:
            if curr.id == queryID:
                if not prev:
                    self.head = curr.next
                else:
                    prev.next = curr.next
                self.size -= 1
                return True

            prev = curr
            curr = curr.next

        return False

    def find(self, queryID):
        if self.isEmpty():
            print("FIND: no such element exists")
            return None
        curr = self.head
        while curr:
            if curr.id ==queryID:
                return curr
            elif curr.id > queryID:
                return None
            curr = curr.next
        return None

    def print(self):
        curr = self.head
        while curr:
            print(str(curr.id)+" "+str(curr.name)+" ", end="")
            curr = curr.next
        print()


    def write(self, outFile):
        curr = self.head
        while curr:
            outFile.write(str(curr.id) + " " + str(curr.name) + " ")
            curr = curr.next
        outFile.write("\n")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise Exception("Correct usage: [program] [input] [output]")

    course = Course()
    with open(sys.argv[1], 'r') as inFile:
        lines = inFile.readlines()
    with open(sys.argv[2], 'w') as outFile:
        for line in lines:
            words = line.split()
            op = words[0]
            if op == ADD:
                if len(words) != 3:
                    raise Exception("ADD: invalid input")
                i, n = int(words[1]), words[2]
                if course.addStudent(i, n):
                    course.write(outFile)
                else:
                    outFile.write("Addition failed\n")
            elif op == DELETE:
                if len(words) != 2:
                    raise Exception("DELETE: invalid input")
                i = int(words[1])
                if course.deleteStudent(i):
                    course.write(outFile)
                else:
                    outFile.write("Deletion failed\n")
            elif op == FIND:
                if len(words) != 2:
                    raise Exception("DELETE: invalid input")
                i = int(words[1])
                found = course.find(i)
                if not found:
                    outFile.write("Search failed\n")
                else:
                    outFile.write(str(found.id) + " " + found.name + "\n")
            else:
                raise Exception("Undefined operator")


