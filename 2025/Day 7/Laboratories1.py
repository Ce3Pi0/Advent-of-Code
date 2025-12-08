FILENAME: str = "Input.txt"

def main() -> None:

    count: int = 0
    beams_indexes: dict[int, bool] = {}

    with open(FILENAME, 'r') as file:
        for line in file.readlines():
            line = line.rstrip()

            temp_beams_indexes: dict[int, bool] = beams_indexes.copy()
            line_len: int = len(line)
            
            for i in range(line_len):
                char: str = line[i]
                
                if char == 'S': 
                    temp_beams_indexes[i] = True
                elif char == '^' and i in beams_indexes:
                    if not beams_indexes[i]: continue
                    if i - 1 < 0 or i + 1 >= line_len: continue
                    
                    temp_beams_indexes[i] = False
                    temp_beams_indexes[i - 1] = True
                    temp_beams_indexes[i + 1] = True
                    count += 1
            
            beams_indexes = temp_beams_indexes.copy()
        print(count)

if __name__ == "__main__":
    main()