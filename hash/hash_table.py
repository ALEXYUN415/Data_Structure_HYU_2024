import sys

TWO_SUM = 'T'
SYMMETRIC_PAIRS = 'S'

def readIntegers(n: int, s: str) -> list:
    words = s.split()
    assert(len(words) == n)
    arr = [int(w) for w in words]
    return arr

def two_sum(k, nums):
    num_set = set()
    for num in nums:
        if k - num in num_set:
            return "T"
        num_set.add(num)
    return "F"

def symmetricpairs(pairs):
    pair_check = {}  # 각 쌍의 첫 번째를 key로, 두 번째 를 value로 저장하는 Dictionary
    result = []  # 대칭되는 쌍을 저장할 리스트
    for a, b in pairs:  # 입력된 쌍을 탐색
        if b in pair_check and pair_check[b] == a:  # 현재 (a, b)에 대해 b가 dict에 있고 b값이  딕셔너리 안에 a와 같은게 있는지 확인
            result.append((b, a))  # 있다고 한다면 대칭되는 (b, a)를 result에 추가

        pair_check[a] = b  # 현재 쌍을 dict에 추가, a를 key b를 value로 저장
    return result  # 대칭 쌍이 담긴 결과 리스트를 반환

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
            if op == TWO_SUM:
                if len(words) != 3:
                    raise Exception("TWO_SUM: invalid input")
                k, n = int(words[1]), int(words[2])
                i += 1

                nums = readIntegers(n, lines[i])
                result = two_sum(k, nums)
                outFile.write(result + '\n')

            elif op == SYMMETRIC_PAIRS:
                if len(words) != 2:
                    raise Exception("SYMMETRIC_PAIRS: invalid input")
                n = int(words[1])
                pairs = []
                while n:
                    i += 1
                    words = lines[i].split()
                    if len(words) != 2:
                        raise Exception("SYMMETRIC_PAIRS: invalid input")
                    a, b = int(words[0]), int(words[1])
                    pairs.append((a, b))
                    n -= 1

                result_pairs = symmetricpairs(pairs)
                result_str = ' '.join([f'{a} {b}' for a, b in result_pairs])
                outFile.write(result_str + '\n')
            else:
                raise Exception("Undefined operator")
            i += 1