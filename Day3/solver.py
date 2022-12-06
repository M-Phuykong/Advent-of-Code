
def main():
    
    input_file = "Day3/input.txt"
    res = 0
    # upper case Ascii: 65 - 90 (minus 96)
    # lower case Ascii: 97 122 (minus 38)

    with open(input_file) as f:
        lines = f.readlines()
    
    for i in range(3, len(lines) + 3, 3):
        sack = lines[i - 3:i]

        first_sack = sack[0].strip()
        second_sack = sack[1].strip()
        third_sack = sack[2].strip()

        answ = next(iter(set(first_sack).intersection(second_sack, third_sack)))

        # uppercase
        #
        if (65 <= ord(answ) <= 90):
            res += (ord(answ) - 38)

        # lower case
        #
        else:
            res += (ord(answ) - 96)

    print(res)




if __name__ == "__main__":
    main()