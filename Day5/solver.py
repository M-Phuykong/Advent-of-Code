
def main():
    
    input_file = "Day5/input.txt"
    res = 0
    crates = [[] for _ in range(10)]
    instr = []

    with open(input_file) as f:
        lines = f.readlines()

    # get crate ordering
    #
    for i in range(8):
        ind = 0

        for j in range(0, 36, 4):
            box = lines[i][j:j+4]
            ind +=1
            if "[" in box:
                crates[ind].append(box[1])

    # reverse crane ordering
    #
    for i in range(len(crates)):
        crates[i] = crates[i][::-1]

    # get instruction
    #
    for i in range(10, len(lines)):
        line = lines[i].replace(" ", "").replace("move","").replace("from"," ").replace("to", " ")
        instr.append((tuple(map(int,line.split()))))

    # execute each instruction
    #
    for ind, ins in enumerate(instr):

        to_move = crates[ins[1]][-ins[0]:]
        
        for i in range(ins[0]):
            crates[ins[1]].pop()
        
        # part 1
        #
        crates[ins[2]].extend(to_move[::-1])

        # part 2
        #
        # crates[ins[2]].extend(to_move)

    res = "".join(c[-1] for c in crates[1:])

    print(res)

if __name__ == "__main__":
    main()