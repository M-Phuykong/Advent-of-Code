from collections import Counter

def main():
    
    input_file = "Day6/input.txt"
    with open(input_file) as f:
        lines = f.readlines()
    s = lines[0]

    # part 1
    #
    # part 2: change all the 4 to 14
    #
    for ind, char in enumerate(s[14:len(s)],14):
        start_window = set(Counter(s[ind - 14 :ind]).keys())

        if len(start_window) == 14:
            res = ind
            break

    print(res)
    


if __name__ == "__main__":
    main()