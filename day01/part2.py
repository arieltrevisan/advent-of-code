import string
from util import file_util

def day01_part2():
    lines = file_util.read_file_lines("day01/input.txt")

    lineNum = 0
    count = 0

    for n in range(0, len(lines)):
        if (len(lines) <= n+2): 
            continue

        current1 = int(lines[n])
        current2 = int(lines[n+1])
        current3 = int(lines[n+2])
        currentSum = current1 + current2 + current3
        lineNum += 1

        if (lineNum == 1):
            prev1 = current1
            prev2 = current2
            prev3 = current3
            print(f"{lineNum}: {currentSum} (N/A - no previous sum)")
            continue
        
        prevSum = prev1 + prev2 + prev3
        if (prevSum < currentSum):
            print(f"{lineNum}: {currentSum} (increased)")
            count += 1
        elif (prevSum == currentSum):
            print(f"{lineNum}: {currentSum} (no change)")
        else:
            print(f"{lineNum}: {currentSum} (decreased)")
        
        prev1 = current1
        prev2 = current2
        prev3 = current3

    print(f"Total Sums: {lineNum}")
    print(f"Greater Sums: {count}")
