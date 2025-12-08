FILENAME: str = "Input.txt"

def main() -> None:
    with open(FILENAME) as file:
        file_lines = file.readlines()
        lines_count = len(file_lines)
        line_size: int = len(file_lines[len(file_lines) - 1])

        total: int = 0
        sub_totals: list[int] = [0, 1]

        for i in range(len(file_lines)):
            file_lines[i] = file_lines[i].replace("\n", '')

        for i in range(line_size - 1, -1, -1):
            updated: bool = False
            temp_num: int = 0

            for j in range(lines_count - 1):
                ch = file_lines[j][i]
                if ch.isdigit():
                    updated = True
                    temp_num *= 10
                    temp_num += int(ch) 

            if updated:
                sub_totals[0] += temp_num
                sub_totals[1] *= temp_num

            match file_lines[j + 1][i]:
                case '+':
                    total += sub_totals[0]
                    sub_totals = [0, 1]
                case '*':
                    total += sub_totals[1]
                    sub_totals = [0, 1]
                case _:
                    pass
            
        print(total)

if __name__ == "__main__":
    main()