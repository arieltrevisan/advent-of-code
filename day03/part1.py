from util import file_util

def day03_part1(sampleInput = False):
    lines = file_util.read_file_lines(f"day03/input{'Sample' if sampleInput else ''}.txt")

    oneSum = []
    for line in lines:
        lineArray = [char for char in line]

        i = 0
        for c in lineArray:
            if (len(oneSum) <= i):
                oneSum.append(0)
            oneSum[i] += 1 if c == "1" else 0
            i += 1

    i = 0
    binsGamma = [False] * len(oneSum)
    binsEpsilon = [False] * len(oneSum)
    half = len(lines) / 2
    
    for c in oneSum:
        binsGamma[i] = True if (c >= half) else False
        binsEpsilon[i] = not binsGamma[i]
        i += 1

    gamma = ["1" if n == True else "0" for n in binsGamma]
    epsilon = ["1" if n == True else "0" for n in binsEpsilon]

    gammaStr = "".join(gamma)
    epsilonStr = "".join(epsilon)

    gammaInt = int(gammaStr, base=2)
    epsilonInt = int(epsilonStr, base=2)

    print(f"Total Lines: {len(lines)}")
    print(f"Sums of 1s: {oneSum}")
    
    print(f"Gamma booleans: {binsGamma}")
    print(f"Gamma binaries: {gamma}")
    print(f"Gamma integer: {gammaInt}")
    
    print(f"Epsilon booleans: {binsEpsilon}")
    print(f"Epsilon binaries: {epsilon}")
    print(f"Epsilon integer: {epsilonInt}")

    print(f"Gamma * Epsilon = {(gammaInt * epsilonInt)}")
