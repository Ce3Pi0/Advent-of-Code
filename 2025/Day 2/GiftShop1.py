FILENAME: str = "Input.txt"

def get_digit_count(num: int) -> int:
    count = 0
    while num > 0:
        num //= 10
        count += 1

    return count

def count_repeating(start_num: int, end_num: int) -> int:
    sum: int = 0

    for i in range(start_num, end_num + 1):
        digit_cnt: int = get_digit_count(i) 
        if digit_cnt % 2 != 0:
            i = int('9' * digit_cnt)
            continue

        text_num: str = str(i)
        first_part, second_part = text_num[:len(text_num)//2], text_num[len(text_num)//2:]
        if first_part == second_part:
            sum += i

    return sum

def main() -> None:
    total: int = 0
    
    with open(FILENAME, "r") as file:
        for line in file.readlines():
            line = line.rstrip().split('\n')
            line = line[0].split(',')
            # line.pop()

            for pair in line:
                pair = pair.split('-')
                start_num: int = int(pair[0])
                end_num: int = int(pair[1])

                total += count_repeating(start_num, end_num)
    print(total)        

if __name__ == "__main__":
    main()