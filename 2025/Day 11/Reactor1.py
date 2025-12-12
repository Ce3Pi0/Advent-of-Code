from collections import deque

FILENAME: str = "Input.txt"

def count_paths(n: int, graph: list, source: int, destination: int) -> int:
    in_degree: list[int] = [0] * (n + 1)

    for neighbors in graph:
        for neighbor in neighbors:
            in_degree[neighbor] += 1

    dq: deque = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            dq.append(i)

    order: list[int] = []
    while dq:
        node = dq.popleft()
        order.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                dq.append(neighbor)

    ways: list[int] = [0] * (n + 1)
    ways[source] = 1

    for node in order:
        for neighbor in graph[node]:
            ways[neighbor] += ways[node]

    return ways[destination]

def parse_file() -> tuple[dict[str, list[str]], dict[str, int]]:
    hashed_graph: dict[str, list[str]] = {}
    hashed_elements: dict[str, int] = {}
    
    with open(FILENAME, 'r') as file:        
        all_lines: list[str] = file.readlines() 
        for i in range(1, len(all_lines) + 1):
            line = all_lines[i - 1].rstrip()
            
            node: str = line.split(": ")[0] 
            neigh: list[str] = line.split(' ')[1:]

            hashed_elements[node] = i
            hashed_graph[node] = neigh

    return (hashed_graph, hashed_elements)

def parse_graph(hashed_graph: dict[str, list[str]], hashed_elements: dict[str, int]) -> list:
    n: int = len(hashed_elements)
    final_destination: int = n + 1
    graph: list = [[] for _ in range(n + 1)]

    for hashed_element in hashed_elements:
        neighbors: list[int] = []
        for hashed_neighbor in hashed_graph[hashed_element]:
            if hashed_neighbor != "out":
                neighbors.append(hashed_elements[hashed_neighbor])
            else:
                neighbors.append(final_destination)
        graph[hashed_elements[hashed_element]] = neighbors
    graph.append([])
    
    return graph

def main() ->  None:

    hashed_graph, hashed_elements = parse_file()
    graph: list = parse_graph(hashed_graph, hashed_elements)

    n: int = len(hashed_elements)
    source = hashed_elements["you"]
    destination = n + 1

    total: int = count_paths(n + 1, graph, source, destination)

    print(total)

if __name__ == "__main__":
    main()
