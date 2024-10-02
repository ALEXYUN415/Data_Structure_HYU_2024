import sys

BINARY_SEARCH = 'B'
PERFECT_SQUARE = 'P'


def binary_search(arr, target):
    start = 0
    end =len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

def perfect_square(n):
    if n == 1:
        return True
    start = 1
    end = n

    while start <= end:
        mid = (start + end) // 2
        if mid * mid == n:
            return True
        elif mid * mid < n:
            start = mid + 1
        else:
            end = mid - 1
    return False


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise Exception("Correct usage: [program] [input] [output]")
    with open(sys.argv[1], 'r') as inFile:
        lines = inFile.readlines()
    with open(sys.argv[2], 'w') as outFile:
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            words = line.split()
            op = words[0]

            if op == BINARY_SEARCH:
                if len(words) != 3:
                    raise Exception("BINARY_SEARCH: invalid input")
                size, x = int(words[1]), int(words[2])
                i += 1
                sequence = list(map(int, lines[i].strip().split()))

                outFile.write(f"B {size} {x}\n")

                result = binary_search(sequence, x)
                if result is None:
                    outFile.write("N\n")
                else:
                    outFile.write(f"{result}\n")

            elif op == PERFECT_SQUARE:
                if len(words) != 2:
                    raise Exception("PERFECT_SQUARE: invalid input")
                x = int(words[1])
                if perfect_square(x):
                    outFile.write("T\n")
                else:
                    outFile.write("F\n")
            i += 1
