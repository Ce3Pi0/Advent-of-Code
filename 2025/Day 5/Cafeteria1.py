FILENAME: str = "Input.txt"

def search_ranges(valid_ranges: list[str], value: int) -> bool:
    valid_ranges.sort()
    
    for valid_range in valid_ranges:
        valid_range = valid_range.split('-')
        lower_range: int = int(valid_range[0])
        upper_range: int = int(valid_range[1])

        if value >= lower_range and value <= upper_range:
            return True

    return False

def main() -> None:
    valid_ranges: list[str] = []
    count: int = 0

    with open(FILENAME) as file:
        checking: bool = False

        for line in file.readlines():
            line = line.rstrip()

            if len(line) < 1:
                checking = True
                continue
            
            if checking:
                count += 1 if search_ranges(valid_ranges, int(line)) else 0
            else:
                valid_ranges.append(line)
    
    print(count)

if __name__ == "__main__":
    main()