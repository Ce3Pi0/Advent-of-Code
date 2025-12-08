FILENAME: str = "Input.txt"

def main() -> None:
    start_pos: int = 50
    count: int = 0

    with open(FILENAME) as file:
        for line in file:
            striped_line:str = line.rstrip()

            if len(striped_line) <= 1: raise RuntimeError(f"Issue with the line: {striped_line}")
            direction = striped_line[0]
            try:
                value: int = int(striped_line[1:])
            except:
                Warning(f"An error occurred while trying to convert the second part of {striped_line} to an integer.")
                return

            match direction:
                case 'L':
                    start_pos -= value
                case 'R':
                    start_pos += value
                case _:
                    raise RuntimeError(f"Invalid starting character of line {striped_line}")
            

            # Reset dial position
            if start_pos < 0:
                temp = start_pos % 100
                start_pos = temp
            start_pos %= 100
            
            # Increase zeros counter if start_pos is 0
            if start_pos == 0:
                count += 1

    print(count)

if __name__ == "__main__":
    main()