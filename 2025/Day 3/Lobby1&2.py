FILENAME: str = "Input.txt"
# Joltage value based on the problem
JOLTAGE_SIZE: int = 12

def sum_joltages(l: list[int]) -> int:
    if len(l) != JOLTAGE_SIZE:
        raise RuntimeError("List size too big")
    
    l.reverse()

    sum = 0
    mult = 1
    for el in l:
        if el < 0:
            raise RuntimeError("Negative Joltage values not accepted")
        sum += el * mult
        mult *= 10
    return sum

def main()-> None:
    with open(FILENAME) as file:
        l: list[int] = []
        res: int = 0

        for line in file:
            striped_line: list = line.rstrip()
            
            index: int = 0
            pos: int = 0
            # Loop until the l list reaches the JOLTAGE_SIZE size which is needed for the problem
            while len(l) < JOLTAGE_SIZE:
                # The numbers that can be considered for choosing the current number (first to last number) are in the range {index : length of line - JOLTAGE_SIZE + pos} where the pos is the position of the current element in the joltages list
                if index > len(striped_line) - JOLTAGE_SIZE + pos:
                    raise RuntimeError("Index cannot be greater than limit")
                
                # Sub list with only the accessible joltages from the line (starting from the previous element's index + 1 - starting index is 0 and index updates each time a max element is chosen)
                sub_list: list[str] = striped_line[index : len(striped_line) - (JOLTAGE_SIZE - 1) + pos]
                
                # Find the  max element from the sub list
                max_num: int = int(max(sub_list))

                # Get the max element's index
                index = sub_list.index(str(max_num)) + index + 1
                
                # Increase the pos counter which is equal to the joltages list size
                pos += 1
                # Add the max element to the joltages list
                l.append(max_num)
            
            # Sum the joltages list each line and clear the list afterwards
            res += sum_joltages(l)
            l = []
    
    print(res)

if __name__ == "__main__":
    main()