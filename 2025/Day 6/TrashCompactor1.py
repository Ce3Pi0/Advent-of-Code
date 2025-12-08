FILENAME: str = "Input.txt"
def main() -> None:
    with open(FILENAME) as file:
        
        sums_and_products: list[list[int]] = []
        total: int = 0

        for line in file.readlines():
            line: str = line.rstrip().rsplit()

            line_size: int = len(line)
            
            if str(line[0]).isdigit():
                for i in range(line_size):
                    if (len(sums_and_products) != line_size):
                        sums_and_products.append([int(line[i]), int(line[i])])
                    else:
                        sums_and_products[i][0] += int(line[i])
                        sums_and_products[i][1] *= int(line[i])
            else:
                for i in range(line_size):
                    match line[i]:
                        case '+': total += sums_and_products[i][0]
                        case '*': total += sums_and_products[i][1]
                        case _: break
        print(total)

if __name__ == "__main__":
    main()