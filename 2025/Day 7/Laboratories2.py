FILENAME: str = "Input.txt"

def count_combinations(lines: list[str], current_line_index: int = 0, beam_index: int = -1, memo: dict[str, int] = None) -> int:
    if memo is None:
        memo = {}

    if str(current_line_index) + ',' + str(beam_index) in memo:
        return memo[str(current_line_index) + ',' + str(beam_index)]
    
    if current_line_index >= len(lines) - 1:
        memo[str(len(lines)) + ',' + str(beam_index)] = 1
        return 1

    left_count = 0
    right_count = 0
    total_count = 0

    current_line: list[str] = lines[current_line_index]

    char: str = current_line[beam_index] 

    if char == '^':
        if beam_index - 1 >= 0:
            left_count += count_combinations(lines, current_line_index + 2, beam_index - 1, memo)
        if beam_index < len(current_line):
            right_count += count_combinations(lines, current_line_index + 2, beam_index + 1, memo)
    else:
        total_count += count_combinations(lines, current_line_index + 1, beam_index, memo)
    
    if str(current_line_index) + ',' + str(beam_index) in memo.keys():
        memo[str(current_line_index) + ',' + str(beam_index)] += total_count + left_count + right_count
    else:
        memo[str(current_line_index) + ',' + str(beam_index)] = total_count + left_count + right_count
    return total_count + left_count + right_count

def main() -> None:

    count: int = 0

    with open(FILENAME, 'r') as file:
        trimmed_lines: list[str] = []

        s_index = -1

        for line in file.readlines():
            if 'S' in line:
                s_index = line.index('S')

            trimmed_lines.append(line.rstrip())

        count = count_combinations(trimmed_lines, current_line_index=2, beam_index=s_index)

        print(count)

if __name__ == "__main__":
    main()