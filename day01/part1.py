from util import file_util

def day01_part1():
    lines = file_util.read_file_lines("day01/input.txt")

    lineNum = 0
    count = 0
    for line in lines:
        current = int(line)
        lineNum += 1

        if (lineNum == 1): 
            prev = current
            print(f"{lineNum}: {line} (N/A - no previous sum)")
            continue
        
        if (prev < current):
            print(f"{lineNum}: {line} (increased)")
            count += 1
        else:
            print(f"{lineNum}: {line} (decreased)")
        
        prev = current
    
    print(f"Total Lines: {lineNum}")
    print(f"Greater Than Previous: {count}")