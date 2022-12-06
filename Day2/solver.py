
def main():
    
    input_file = "Day2/input.txt"
    score = {"X" : 0, "Y": 3, "Z":6}
    res = 0

    with open(input_file) as f:
        lines = f.readlines()
    
    for line in lines:
        opponent, you = line.split()

        if opponent == "A": # rock
        
            if you == "X":
                res += 3
            elif you == "Y":
                res += 1
            else:
                res += 2

        elif opponent == "B": # paper
            
            if you == "X":
                res += 1
            elif you == "Y":
                res += 2
            else:
                res += 3
        
        else: # scissor
                        
            if you == "X":
                res += 2
            elif you == "Y":
                res += 3
            else:
                res += 1

        res += score[you]

    print(res)




if __name__ == "__main__":
    main()