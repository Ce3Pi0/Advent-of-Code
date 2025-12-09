from __future__ import annotations
import math
import sys

FILENAME: str = "Input.txt"

class Vertex:
    def __init__(self, x: int, y: int, z: int):
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
        return math.sqrt((abs(dest._x - src._x)**2) + (abs(dest._y - src._y) ** 2) + (abs(dest._z - src._z) ** 2))


def main() -> None:
    adjacency_list: dict[Vertex, Vertex | None] = dict()

    with open(FILENAME) as file:
        for line in file.readlines():
            line = line.rstrip().split(',')

            if len(line) != 3: raise RuntimeError("Line doesn't have 3 coordinates.")

            new_vertex: Vertex = Vertex(int(line[0]), int(line[1]), int(line[2]))

            if new_vertex not in adjacency_list.keys():
                adjacency_list[new_vertex] = None
            
    # ACTUAL LOGIC
    # make connections
    connections: int = 0
    MAX_CONNECTIONS: int = 10
    
    keys: list[Vertex] = list(adjacency_list.keys())

    while connections < MAX_CONNECTIONS:
        for i in range(len(keys)):
            current_vertex: Vertex = keys[i]
            if not adjacency_list[current_vertex]:
                continue

            min_dist: float = sys.maxsize
            connector: Vertex | None = None
            
            for j in range (len(keys)):
                cur_dist: float = Vertex.calc_dist_3d(current_vertex, keys[j]) 
                if cur_dist < min_dist and current_vertex != keys[j]:
                    min_dist = cur_dist
                    connector = keys[j]

            if connector is not None:
                adjacency_list[connector].append(keys[i])
                adjacency_list[keys[i]].append(connector)

    print(adjacency_list)
    # create segments

    # count segment lengths


if __name__ == "__main__":
    main()