
def main():
    
    input_file = "Day4/input.txt"
    res = 0

    with open(input_file) as f:
        lines = f.readlines()
    
    for line in lines:
        pairs = line.strip().split(",")
        pair1 = tuple(pairs[0].split("-"))
        pair2 = tuple(pairs[1].split("-"))

        if (int(pair2[0]) <= int(pair1[1]) and int(pair2[0]) >= int(pair1[0])) or (int(pair1[0]) <= int(pair2[1]) and int(pair1[0]) >= int(pair2[0])):
            res +=1
            
    print(res)

if __name__ == "__main__":
    main()