FILENAME: str = "Input.txt"
MAX_ADJ_COUNT: int = 4

def calc_adj_count(grid: list[list[str]], i: int, j: int) -> int:
    if i < 0 or i >= len(grid): return 0
    if j < 0 or j >= len(grid[i]): return 0
    if grid[i][j] == '@': return 1
    
    return 0

def main() -> None:
    count: int = 0
    
    grid: list[list[str]] = []

    with open(FILENAME) as file:
        for line in file.readlines():
            grid.append(list(line.rstrip()))

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '.': continue

                adj_count = 0

                adj_count += calc_adj_count(grid, i - 1, j - 1)
                adj_count += calc_adj_count(grid, i - 1, j + 1)
                adj_count += calc_adj_count(grid, i - 1, j)
                adj_count += calc_adj_count(grid, i + 1, j)
                adj_count += calc_adj_count(grid, i + 1, j - 1)
                adj_count += calc_adj_count(grid, i + 1, j + 1)
                adj_count += calc_adj_count(grid, i, j + 1)
                adj_count += calc_adj_count(grid, i, j - 1)

                if adj_count < MAX_ADJ_COUNT: 
                    count += 1
    print(count)
if __name__ == "__main__":
    main()