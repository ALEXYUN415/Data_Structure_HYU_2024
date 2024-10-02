# Practice 10. Graph Representation
import sys
from collections import deque

CONSTRUCT = 'C'
IS_ADJACENT = 'I'
GET_NEIGHBORS = 'N'
BFS = 'B'
DFS = 'D'
REACHABILITY = 'R'
TOPOLOGICAL_SORT = 'T'
SHORTEST_PATH = 'S'


class Graph:
    def __init__(self):
        self.adj_list = {}  # directed graphs with adjacency lists
        self.weights = {}

    def add_edge(self, u, v, weight):  # 간선 삽입 (삽입할라면 vertex 즉 노드가 있어야 연결할 수 있음)
        if u not in self.adj_list:  # (u 노드가 없는 경우 -> 처음 시작할 노드가 없는경우)
            self.adj_list[u] = []  # 배열에다가 하나 생성
        if v not in self.adj_list:  # v vertex가 없는 경우에는 새로운 배열을 생성
            self.adj_list[v] = []
        self.adj_list[u].append(v)  # 그 배열에 간선 하나 만들기
        self.weights[(u, v)] = weight

    def is_adjacent(self, u, v):
        return v in self.adj_list.get(u, [])  # u가 존재하지 않을때 빈 배열로 반환

    def get_neighbors(self, u):
        return self.adj_list.get(u, [])

#  두 함수의 차이점은 다음과 같다
#  먼저 is_adjacent 함수는 u vertex 기준으로 v vertex로 향하는 간선이 존재하는 경우 반환하는것이고
#  get_neighbors 두 노드 사이가 이웃해있기만한다면 즉 어느한쪽으로만으로도 간선이 있다면 반환해주는 함수이다
if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise Exception("Correct usage: [program] [input] [output]")

    g = Graph()
    with open(sys.argv[1], 'r') as inFile:
        lines = inFile.readlines()
    with open(sys.argv[2], 'w') as outFile:
        i = 0  # 배열의 번호
        while i < len(lines):
            words = lines[i].split()
            op = words[0]
            if op == CONSTRUCT:
                if len(words) != 3:
                    raise Exception("CONSTRUCT: invalid input")
                n, m = int(words[1]), int(words[2])  # n은 vertex, m은 edge
                cnt, data = m, []
                # TODO. Construct a graph
                for _ in range(m):  # m번 즉 edge수 만큼 반복 (파이썬에서 _는 범용적으로 사용)
                    edge = lines[i + 1].split()  # 문자열 나누기
                    u, v, weight = int(edge[0]), int(edge[1]), int(edge[2])  # 간선의 시작과 끝 + 가중치 저장하기
                    g.add_edge(u, v, weight)
                    i += 1
            elif op == IS_ADJACENT:
                if len(words) != 3:
                    raise Exception("IS_ADJACENT: invalid input")
                u, v = int(words[1]), int(words[2])  # 간선 위치 할당
                # TODO. Check if edge (u, v) exists in the graph
                outFile.write(str(u) + ' ' + str(v) + ' ' + ('T' if g.is_adjacent(u, v) else 'F') + '\n')
            elif op == GET_NEIGHBORS:
                if len(words) != 2:
                    raise Exception("GET_NEIGHBORS: invalid input")
                u = int(words[1])
                # TODO. Get all the neighbors of u
                outFile.write(' '.join(map(str, g.get_neighbors(u))) + '\n')  # 공백으로 합쳐서 작성
            else:
                raise Exception("Undefined operator")
            i += 1
