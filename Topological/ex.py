# Practice 10. Graph Representation
import heapq
import sys
from collections import deque
from queue import PriorityQueue

CONSTRUCT = 'C'
IS_ADJACENT = 'I'
GET_NEIGHBORS = 'N'
BFS = 'B'
DFS = 'D'
REACHABILITY = 'R'
TOPOLOGICAL_SORT = 'T'
SHORTEST_PATH = 'S'


class Graph:
    # TODO. Define a constructor and proper methods
    def __init__(self):
        self.graph = dict()
        self.weight = dict()

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.weight[(u, v)] = weight

    def is_adjacent(self, u, v):
        return v in self.graph.get(u, [])
        # dict.get() 메서드는 지정한 키가 딕셔너리에 없는 경우 기본값을 반환합니다.
        # 물론 self.graph[u]로 접근 가능하지만 u가 딕셔너리에 없을 때 오류 발생.
        # 이 기본값은 인자를 두 개 받는 경우 첫 번째 인자는 키, 두 번째 인자는 기본값입니다. 두 번째 인자를 제공하지 않으면 None을 기본값으로 반환합니다.
        # get함수를 사용하여 u가 graph에 없는 경우도 처리 완료!
        # in 연산자: in 연산자는 None에 대해 항상 False를 반환합니다.
        # in 연산자를 통해 v가 u의 value값이 아닐 때도 처리 완료!


    def get_neighbors(self, u):
        return self.graph.get(u, [])

    def dfs(self, graph, v):
        visited = [False] * len(graph)
        visited[v] = True
        outFile.write(str(v) + " ")
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs(graph, i)

        # 깊이 우선 탐색 -> 재귀 함수 이용하자
        # 맨 위 노드를 넣고, 그 노드의 value값들을 탐색
        # 탐색한 노드들은 True를 할당해주고, 만약 False라면 재귀적으로 다시 탐색

    def bfs(self, graph, start):
        # start 원소를 가지고 있는 큐를 하나 생성 ( 보통 맨 위 노드가 된다.)
        # 우선 우리는 start 원소의 이웃들을 모두 돌아야 한다.
        # 딕셔너리의 value 값에 접근하자.
        # 큐에 start 원소를 pop 해주고, value 값들을 append 해주고
        # 그 value 값들에 대해 또 다시 pop 해주면서 append 과정 반복

        visited = set()
        queue = deque([start])
        while queue:
            v = queue.popleft()
            if v not in visited:
                visited.add(v)
                outFile.write(str(v) + " ")
                for i in self.graph[v]:
                    if i not in visited:
                        queue.append(i)

    def reachability(self, start, target):
        # 시작노드에서 타겟노드까지 도달 가능한가?
        # 방문한 노드들을 저장하는 집합을 하나 설정하자.
        # 굳이 집합을 설정하는 이유는? 사이클이 있는 그래프의 경우 무한 루프가 발생할 수도 있다.
        # 방문 방식은 깊이 탐색으로 할 것.
        # 만약 방문한 노드가 target 이라면? True를 리턴.
        # 아니라면? 그 노드의 value 값들을 탐색해보자.
        # value 값에 target이 없다면?
        # value 값들을 대상으로
        visited = set()

        def dfs(v):
            if v == target:
                return True
            visited.add(v)
            for i in self.graph.get(v, []):
                if i not in visited:
                    visited.add(i)
                    if dfs(i):
                        return True
            return False

        return dfs(v)

    def topological_sort(self):
        # 진입 차수가 0인 노드들만 큐에 삽입
        # 그 노드는 그래프에서 빠졌다고 생각
        # 그렇다면 그 노드의 이웃 노드들의 진입 차수는 하나씩 빠진다
        # 다음 노드 중 진입 차수가 0인 노드들을 큐에 삽입
        # 이 과정을 반복하자.
        indegree = {node: 0 for node in self.graph}
        for u in self.graph:
            for v in self.graph[u]:
                indegree[v] += 1

        queue = deque([node for node in indegree if indegree[node] == 0])
        sorted_nodes = []

        while queue:
            v = queue.popleft()
            sorted_nodes.append(v)
            for i in self.graph.get(v, []):
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)

        if len(sorted_nodes) != len(self.graph):
            raise Eroor("Cycle error")
        return sorted_nodes

    def shortest_path(self, start, target):
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        priority_queue = [(0, start)]
        previous = {}

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            # 현재 노드까지의 거리가 이미 기록된 거리보다 크다면 무시
            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight

                # 더 짧은 경로를 발견하면, 거리 업데이트 및 큐에 추가
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
                    previous[neighbor] = current_node

        path = []
        current = target
        while current != start:
            path.append(current)
            current = previous[current]
        path.append(start)
        return path[::-1]


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
                result = 'T' if g.is_adjacent(u, v) else 'F'
                outFile.write(f"{u} {v} {result}\n")

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
                ans = g.bfs(v)
                outFile.write(' '.join(map(str, ans)) + '\n')

            elif op == DFS:
                if len(words) != 2:
                    raise Exception("DFS: invalid input")
                v = int(words[1])
                ans = g.dfs(v)
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
                if path is None:
                    outFile.write("No path\n")
                else:
                    outFile.write(' '.join(map(str, path)) + '\n')

            else:
                raise Exception("Undefined operator")
            i += 1