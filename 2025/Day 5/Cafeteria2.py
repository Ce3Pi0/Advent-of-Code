FILENAME: str = "Input.txt"

def find_ranges(valid_ranges: list[str], value: int) -> tuple[int]:
    valid_ranges.sort()
    
    for valid_range in valid_ranges:
        valid_range = valid_range.split('-')
        lower_range: int = int(valid_range[0])
        upper_range: int = int(valid_range[1])

        if value >= lower_range and value <= upper_range:
            return (lower_range, upper_range)
    return (-1, -1)

def insert_ranges(valid_ranges: list[str], test_range: str) -> None:
    valid_ranges.sort()
    
    test_range = test_range.split('-')
    lower_test_range: int = int(test_range[0])
    upper_test_range: int = int(test_range[1])

    if upper_test_range < lower_test_range: raise RuntimeError(f"Invalid ranges lower: {lower_test_range} - higher: {upper_test_range}")

    if len(valid_ranges) == 0: valid_ranges.append(str(lower_test_range) + '-' + str(upper_test_range))

    for i in range(len(valid_ranges)):
        valid_range = valid_ranges[i]
        
        valid_range = valid_range.split('-')
        lower_range: int = int(valid_range[0])
        upper_range: int = int(valid_range[1])

        if upper_test_range <= upper_range and lower_test_range >= lower_range:
            return
        elif upper_test_range <= upper_range and upper_test_range >= lower_range:
            found_ranges: tuple[int] = find_ranges(valid_ranges, lower_test_range)
            if found_ranges[0] == -1 and found_ranges[1] == -1:
                lower_range = lower_test_range
            else:
                lower_range = found_ranges[1] + 1
            
            valid_ranges[i] = str(lower_range) + '-' + str(upper_range)

            return
        elif lower_test_range >= lower_range and lower_test_range <= upper_range:
            found_ranges: tuple[int] = find_ranges(valid_ranges, upper_test_range)
            if found_ranges[0] == -1 and found_ranges[1] == -1:
                upper_range = upper_test_range
            else:
                upper_range = found_ranges[0] - 1
            
            valid_ranges[i] = str(lower_range) + '-' + str(upper_range)

            return
        elif lower_test_range < lower_range and upper_test_range > upper_range:
            found_ranges: tuple[int] = find_ranges(valid_ranges, upper_test_range)
            if found_ranges[0] == -1 and found_ranges[1] == -1:
                lower_range = lower_test_range
                upper_range = upper_test_range
            else:
                upper_range = found_ranges[0] - 1
                lower_range = found_ranges[1] + 1

            valid_ranges[i] = str(lower_range) + '-' + str(upper_range)

            return

    valid_ranges.append(str(lower_test_range) + '-' + str(upper_test_range))

def sum_ranges(ranges: list[str]) -> int:
    sum: int = 0

    for r in ranges:
        valid_range = r.split('-')
        lower_range: int = int(valid_range[0])
        upper_range: int = int(valid_range[1])

        sum += upper_range - lower_range + 1

    return sum

def main() -> None:
    valid_ranges: list[str] = []

    with open(FILENAME) as file:

        for line in file.readlines():
            line = line.rstrip()

            insert_ranges(valid_ranges, line)
    
    print(sum_ranges(valid_ranges))

if __name__ == "__main__":
    main()