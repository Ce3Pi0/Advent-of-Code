FILENAME: str = "Input.txt"

def get_digit_count(num: int) -> int:
    count = 0
    while num > 0:
        num //= 10
        count += 1

    return count

def count_repeating(start_num: int, end_num: int) -> int:
    total: int = 0
    start_digit_count: int = get_digit_count(start_num)
    end_digit_count: int = get_digit_count(end_num)

    if start_digit_count == end_digit_count and start_digit_count % 2 != 0: return 0

    if start_digit_count % 2 != 0:
        start_num = pow(10, start_digit_count)

    if end_digit_count % 2 != 0:
        end_num = '9' * (end_digit_count - 1)
        end_num = int(end_num)

    start_digits = list(str(start_num))           
    end_digits = list(str(end_num))
    start_half = start_digit_count // 2
    end_half = end_digit_count // 2                
    
    temp_start_num: int = start_num
    temp_end_num: int = end_num

    start_num = int(start_digits[:start_half][0])
    end_num = int(end_digits[:end_half][0])

    for i in range(start_digit_count, (end_digit_count // 2) + 1):
        temp_max_end_value: int = int('9' * (i - 1))
        end_value: int = min(temp_max_end_value, end_num)

        total += end_value - start_num 
        start_num = pow(10, i)

    return total

def main() -> None:
    total: int = 0
    
    with open(FILENAME, "r") as file:
        for line in file.readlines():
            line: list[str] = line.rstrip().split(',')

            for pair in line:
                if pair == "": break
                pair: list[str] = pair.split('-')
                start_num: int = int(pair[0])
                end_num: int = int(pair[1])

                total += count_repeating(start_num, end_num)
    print(total)        

if __name__ == "__main__":
    main()