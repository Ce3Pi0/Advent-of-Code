import sys

FILENAME: str = "Input.txt"

class Pair:
    def __init__(self, y: int, x: int):
        self._y = y
        self._x = x
    def __repr__(self) -> str:
        return f"x: {self._x}, y: {self._y}"
    
    @property
    def x(self) -> int:
        return self._x
    @property
    def y(self) -> int:
        return self._y

def calc_optimal_area(tile: Pair, tiles: list[Pair], index: int) -> int:
    max_area: int = 0
    for i in range(index + 1, len(tiles)):
        temp_area: int = calc_area(tile, tiles[i]) 
        max_area = temp_area if temp_area > max_area else max_area
            
    return max_area
        
def calc_area(p1: Pair, p2: Pair) -> int:   
    w: int = abs(p1.x - p2.x) + 1
    h: int = abs(p2.y - p1.y) + 1
    
    return w * h

def main() -> None:
    max_area: int = 0
    tiles: list[Pair] = []

    with open(FILENAME) as file:
        for line in file.readlines():
            line = line.rstrip().split(',')
            pair: Pair = Pair(int(line[0]), int(line[1]))
            
            tiles.append(pair)
        for i in range(len(tiles)):
            temp_area: int = calc_optimal_area(tiles[i], tiles, i) 
            max_area = temp_area if temp_area > max_area else max_area

    print(max_area)

if __name__ == "__main__":
    main()