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
        self.graph = {}
        self.weights = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.weights[(u, v)] = weight

    def is_adjacent(self, u, v):
        return v in self.graph.get(u, [])

    def get_neighbors(self, u):
        return self.graph.get(u, [])

    def BFS(self, start):
        result = [] # 마지막에 탐색 결과를 보여주기 위해서 방문하는걸 보여주는 리스트
        q = deque([start]) # 탐색할 노드를 저장할 큐 (deque 사용)
        visited = set([start]) # 이미 방문한 노드를 저장할 집합
        while q: # 큐가 빌 때까지 반복
            node = q.popleft() # 큐에서 노드를 하나 꺼내서 현재 노드로 설정
            result.append(node) # 현재 노드를 결과 리스트에 추가
            for neighbor in self.graph.get(node, []): # 현재 노드의 모든 인접 노드를 탐색
                if neighbor not in visited: # 인접 노드가 방문되지 않았다면
                    visited.add(neighbor) # 인접 노드를 방문한 것으로 표시
                    q.append(neighbor) # 인접 노드를 큐에 추가
        return result # 탐색된 노드의 순서를 반환

    def dfs(self, graph, start):
        visited = [False] * len(graph)  # 방문한 노드를 표시하는 리스트
        visited[start] = True  # 시작 노드를 방문했다고 표시
        outFile.write(str(start) + " ")  # 시작 노드를 출력
        for i in self.graph[start]:  # 시작 노드의 모든 인접 노드에 대해 반복
            if not visited[i]:  # 인접 노드가 방문되지 않았다면
                self.dfs(graph, i)  # 인접 노드를 시작으로 깊이 우선 탐색 수행

    def reachability(self, source, target):
        visited = set()
        def DFS(v):
            if v == target:
                return True
            visited.add(v)
            for neighbor in self.graph.get(v, []):
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
            return False
        return DFS(source)

    def topological_sort(self):
        indegree = {u: 0 for u in self.graph}
        for u in self.graph:
            for v in self.graph[u]:
                indegree[v] += 1
        q = deque([u for u in indegree if indegree[u] == 0])
        result = []

        while q:
            u = q.popleft()
            result.append(u)
            for v in self.graph.get(u, []):
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        return result

    def shortest_path(self, source, target):
        D = {v: float('inf') for v in self.graph}
        D[source] = 0
        P = {v: None for v in self.graph}
        q = deque([source])

        while q:
            u = q.popleft()
            for neighbor in self.graph.get(u, []):
                weight = self.weights[(u, neighbor)]
                distance = D[u] + weight
                if distance < D[neighbor]:
                    D[neighbor] = distance
                    P[neighbor] = u
                    q.append(neighbor)

        path = []
        current = target
        while current is not None:
            path.append(current)
            current = P[current]
        path.reverse()

        return path if path[0] == source else []

if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise Exception("Correct usage: [program] [input] [output]")

    g = Graph()
    with open(sys.argv[1], 'r') as inFile:
        lines = inFile.readlines()

    with open(sys.argv[2], 'w') as outFile:
        i = 0
        while i < len(lines):
            words = lines[i].split()
            op = words[0]
            if op == CONSTRUCT:
                if len(words) != 3:
                    raise Exception("CONSTRUCT: invalid input")
                n, m = int(words[1]), int(words[2])
                for j in range(m):
                    i += 1
                    u, v, w = map(int, lines[i].split())
                    g.add_edge(u, v, w)

            elif op == IS_ADJACENT:
                if len(words) != 3:
                    raise Exception("IS_ADJACENT: invalid input")
                u, v = int(words[1]), int(words[2])
                outFile.write(f"{u} {v} {'T' if g.is_adjacent(u, v) else 'F'}\n")

            elif op == GET_NEIGHBORS:
                if len(words) != 2:
                    raise Exception("GET_NEIGHBORS: invalid input")
                u = int(words[1])
                neighbors = g.get_neighbors(u)
                outFile.write(' '.join(map(str, neighbors)) + '\n')

            elif op == BFS:
                if len(words) != 2:
                    raise Exception("BFS: invalid input")
                v = int(words[1])
                ans = g.BFS(v)
                outFile.write(' '.join(map(str, ans)) + '\n')

            elif op == DFS:
                if len(words) != 2:
                    raise Exception("DFS: invalid input")
                v = int(words[1])
                ans = g.DFS(v)
                outFile.write(' '.join(map(str, ans)) + '\n')

            elif op == TOPOLOGICAL_SORT:
                if len(words) != 1:
                    raise Exception("TOPOLOGICAL_SORT: invalid input")
                ans = g.topological_sort()
                outFile.write(' '.join(map(str, ans)) + '\n')

            elif op == SHORTEST_PATH:
                if len(words) != 3:
                    raise Exception("SHORTEST_PATH: invalid input")
                source, target = int(words[1]), int(words[2])
                path = g.shortest_path(source, target)
                if path:
                    outFile.write(' '.join(map(str, path)) + '\n')
                else:
                    outFile.write("No path\n")

            else:
                raise Exception("Undefined operator")
            i += 1
