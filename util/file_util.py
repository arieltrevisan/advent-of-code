def read_file_lines(path_to_file):
    # reads all lines of a given file
    # strips line ending of each entry
    with open(path_to_file, "r") as file:
        lines = file.readlines()
    return [l.rstrip("\n") for l in lines]