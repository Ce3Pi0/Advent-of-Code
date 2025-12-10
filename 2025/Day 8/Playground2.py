from __future__ import annotations
import math

FILENAME: str = "Input.txt"
MAX_CONNECTIONS: int = 10

class Vertex:
    def __init__(self, index: int, x: int, y: int, z: int):
        self._index = index
        self._x = x
        self._y = y
        self._z = z
    def __repr__(self) -> str:
        return f"(x: {self._x},y: {self._y},z: {self._z})"
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vertex):
            return NotImplemented
        return (self._x, self._y, self._z) == (other.x, other.y, other.z)
    def __hash__(self) -> int:
        return hash((self._x, self._y, self._z))

    @property
    def index(self) -> int:
        return self._index
    @property
    def x(self) -> int:
        return self._x
    @property
    def y(self) -> int:
        return self._y
    @property
    def z(self) -> int:        
        return self._z

    @staticmethod
    def calc_dist_3d(src: "Vertex", dest: "Vertex") -> float:
        return math.sqrt(((dest._x - src._x)**2) + ((dest._y - src._y) ** 2) + ((dest._z - src._z) ** 2))

class VertexPair:
    def __init__(self, src: Vertex, dst: Vertex, dist: float):
        self._src = src
        self._dst = dst
        self._dist = dist
    
    def __repr__(self) -> str:
        return f"V1:{self._src}, V2:{self._dst}, Distance:{self._dist}"

    @property
    def src(self) -> Vertex:
        return self._src
    
    @property
    def dst(self) -> Vertex:
        return self._dst

    @property
    def dist(self) -> float:
        return self._dist

def calculate_distances(vertex: Vertex, vertexes: list[Vertex]) -> list[VertexPair]:
    distances: list[VertexPair] = [] 

    for i in range(vertex.index + 1, len(vertexes)):
        dist: float = Vertex.calc_dist_3d(vertex, vertexes[i])
        
        pair: VertexPair = VertexPair(vertex, vertexes[i], dist)

        distances.append(pair)

    return distances

def find_element(graph: dict[int, list[int]], node: int, dest: int, visited: set[int]) -> bool:
    if node == dest: return True

    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            if find_element(graph, neighbor, dest, visited):
                return True

    return False

def find_element_in_segment(graph: dict[int, list[int]], src: int, dest: int) -> bool:
    visited: set[int] = set()
    if src not in graph or dest not in graph:
        return False

    return find_element(graph, src, dest, visited)

def explore(graph: dict[int, list[int]], node: int, visited: set[int]) -> int:
    stack = [node]
    size = 0

    while stack:
        curr = stack.pop()
        if curr in visited:
            continue
        visited.add(curr)
        size += 1
        for neigh in graph[curr]:
            if neigh not in visited:
                stack.append(neigh)

    return size

def graph_segments(graph: dict[int, list[int]]) -> list[int]:
    visited: set[int] = set()
    island_sizes: list[int] = []
    
    for node in graph.keys():
        if node not in visited:
            island_sizes.append(explore(graph, node, visited))
    
    return island_sizes

def dfs(graph: dict[int, list[int]], current: int, target: int, visited: set[int]) -> bool:
    if current == target:
        return True

    visited.add(current)

    for neighbor in graph[current]:
        if neighbor not in visited:
            if dfs(graph, neighbor, target, visited):
                return True

    return False

def are_connected(graph: dict[int, list[int]], src: int, dest: int) -> bool:
    # If either node has no edges yet, they cannot be connected
    if src not in graph or dest not in graph:
        return False

    return dfs(graph, src, dest, set())

def main() -> None:
    vertexes: list[Vertex] = []
    vertex_pair_distances: list[VertexPair] = [] 

    graph: dict[int, list[int]] = {}

    with open(FILENAME) as file:
        index: int = 0
        for line in file.readlines():
            line = line.rstrip().split(',')

            if len(line) != 3: raise RuntimeError("Line doesn't have 3 coordinates.")

            new_vertex: Vertex = Vertex(index, int(line[0]), int(line[1]), int(line[2]))

            if new_vertex not in vertexes:
                if new_vertex.index not in graph.keys():
                    graph[new_vertex.index] = []
                vertexes.append(new_vertex)
                index += 1
    
    for vertex in vertexes:
        distances: list[VertexPair] = calculate_distances(vertex, vertexes)
        vertex_pair_distances.extend(distances)

    vertex_pair_distances.sort(key=lambda pair: pair.dist)

    # make connections
    for pair in vertex_pair_distances:
        temp = pair

        i: int = pair.src.index
        j: int = pair.dst.index

        if not are_connected(graph, i, j):
            graph[i].append(j)
            graph[j].append(i)
        if len(graph_segments(graph)) == 1:
            print(temp) 
            break

    segments: list[int] = graph_segments(graph)
    segments.sort()



if __name__ == "__main__":
    main()