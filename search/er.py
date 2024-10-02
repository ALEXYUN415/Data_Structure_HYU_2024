# Practice 12. Search
import sys

BINARY_SEARCH = 'B'
PERFECT_SQUARE = 'P'

class Search:
    def __init__(self):
        self.arr = []

    def binary_search(self, outFile, x):
        low = 0
        high = len(self.arr) - 1

        while low <= high:
            mid = (low + high) // 2 # Choice median index for binary search.
            if self.arr[mid] == x:
                outFile.write(f"{mid}\n") # If list value equal target x, write index number in outFile.
                return
            elif self.arr[mid] < x: # Narrow down the scope to find x.
                low = mid + 1
            else:
                high = mid - 1
        outFile.write("N\n") # If do not find x, write 'N' in outFile.

    def perfect_square(self, outFile, x):
        if x < 0: # A negative integer x is invalid input.
            raise Exception("INVALID INPUT: x must be greater than 0")

        low = 0
        high = x

        while low <= high:
            mid = (low + high) // 2 # Choice mid for binary search.
            mid_squared = mid * mid

            if mid_squared == x:
                outFile.write("T\n") # If mid_squared target x, write 'T' in outFile.
                return
            elif mid_squared < x: # Narrow down the scope to find x.
                low = mid + 1
            else:
                high = mid - 1

        outFile.write("F\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise Exception("Correct usage: [program] [input] [output]")
    s = Search()
    with open(sys.argv[1], 'r') as inFile:
        lines = inFile.readlines()
    with open(sys.argv[2], 'w') as outFile:
        i = 0
        while i < len(lines):
            line = lines[i]
            words = line.split()
            op = words[0]
            if op == BINARY_SEARCH:
                if len(words) != 3:
                    raise Exception("BINARY_SEARCH: invalid input")
                size, x = int(words[1]), int(words[2])

                outFile.write(f"B {size} {x}\n")
                i += 1
                words = lines[i].strip() # Stored string with blank characters removed in words variable.
                s.arr = list(map(int, words.split())) # After dividing into spaces, convert each part into an integer and make a list.
                s.binary_search(outFile, x)

            elif op == PERFECT_SQUARE:
                if len(words) != 2:
                    raise Exception("PERFECT_SQUARE: invalid input")
                x = int(words[1])
                s.perfect_square(outFile, x)
            else:
                raise Exception("Undefined operator")
            i += 1
