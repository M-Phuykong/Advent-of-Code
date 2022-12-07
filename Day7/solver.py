from collections import defaultdict
import pprint
from itertools import accumulate

def main():
    
    input_file = "Day7/input.txt"
    MAX = 100_000

    dirs = defaultdict(int)

    with open(input_file) as f:
        lines = f.readlines()
    
    for line in lines:
        match line.split():
            case '$', 'cd', '/': 
                curr = [""]
            case '$', 'cd', "..":
                curr.pop()
            case '$', 'cd', x:
                curr.append(x + "/")
            case '$', 'ls': pass
            case 'dir', _: pass
            case size, name:
                # print(curr)
                for p in accumulate(curr):
                    dirs[p] += int(size)
                # print(dirs)
    # part 1
    #
    # print(sum(val for val in dirs.values() if val <= MAX))

    # part 2
    #
    print(min(dir for dir in dirs.values() if dir >= dirs[""] - 40_000_000))
if __name__ == "__main__":
    main()