
def main():
    
    input_file = "Day1/input.txt"
    res = []

    with open(input_file) as f:
        lines = f.readlines()
    
    cur = 0
    for l in lines:
        if l == "\n":
            res.append(cur)
            cur = 0
        else:
            cur += int(l)

    res.sort(reverse=True)

    print(sum(res[:3]))

if __name__ == "__main__":
    main()