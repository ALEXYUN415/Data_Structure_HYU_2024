# Practice 13. Sorting
import sys

MERGE_SORT = 'M'
QUICK_SORT = 'Q'

def readInput(line, size):
    words = line.split()
    assert (len(words) == size)
    arr = [int(word) for word in words]
    return arr

def mergesort(arr, low, high):
    # 배열이 최대로 쪼개진다면? -> 종료
    if low >= high:
        return
    # 배열을 두 부분으로 분할
    mid = (low + high) // 2
    mergesort(arr, low, mid) # 재귀적으로 계속 나눈다
    mergesort(arr, mid + 1, high)
    # 분할 할때 왼쪽과 오른쪽으로 나눔
    left = arr[low:mid + 1]
    right = arr[mid + 1:high + 1]

    i = 0
    j = 0
    k = low

    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    # 남아 있는 요소들 병합
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

def quicksort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr.pop(0)  # pivot을 맨 앞에 있는걸로 지정
    left = []
    right = []
    for i in arr:
        if i > pivot:
            left.append(i)  # 내림차순이므로 큰값을 왼쪽으로
        else:
            right.append(i)  # 작은값을 오른쪽으로
    return quicksort(left) + [pivot] + quicksort(right)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise Exception("Correct usage: [program] [input] [output]")
    with open(sys.argv[1], 'r') as inFile:
        lines = inFile.readlines()
    with open(sys.argv[2], 'w') as outFile:
        i = 0
        while i < len(lines):
            words = lines[i].split()
            op = words[0]
            if len(words) != 2:
                raise Exception("Error: invalid input")
            size = int(words[1])
            i += 1
            arr = readInput(lines[i], size)
            if op == MERGE_SORT:
                if len(words) != 2:
                    raise Exception("MERGE_SORT: invalid input")
                mergesort(arr, 0, len(arr) - 1)
                for value in arr:
                    outFile.write(str(value) + " ")
                outFile.write("\n")
            elif op == QUICK_SORT:
                if len(words) != 2:
                    raise Exception("QUICK_SORT: invalid input")
                quicksort(arr)
                for value in arr:
                    outFile.write(str(value) + " ")
                outFile.write("\n")
            else:
                raise Exception("Undefined operator")
            i += 1