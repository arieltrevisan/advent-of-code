from util import file_util

def day02_part2(sampleInput = False):
    lines = file_util.read_file_lines(f"day02/input{'Sample' if sampleInput else ''}.txt")

    horizontal = 0
    depth = 0
    aim = 0

    for line in lines:
        values = line.split(" ")
        command = values[0]
        size = int(values[1])

        if (command == "forward"):
            horizontal += size
            depth += size * aim
        elif (command == "up"):
            aim -= size
        elif (command == "down"):
            aim += size
        else:
            raise Exception(f"Unknown command '{command}'")

    print(f"Horizontal: {horizontal}")
    print(f"Depth     : {depth}")
    print(f"Multiply  : {horizontal*depth}")
    