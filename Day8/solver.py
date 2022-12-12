import pprint



def main():
    
    input_file = "Day8/input.txt"

    inp = []
    with open(input_file) as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        inp.append(list(map(int,list(line))))

    ROW, COL = len(inp), len(inp[0])

    def checkBottom(r,c):
        num = 0
        for i in range(r + 1, ROW):
            if inp[i][c] >= inp[r][c]:
                return num + 1
            num += 1
        return num

    def checkTop(r,c):
        num = 0
        for i in range(r - 1, -1, -1):
            if inp[i][c] >= inp[r][c]:
                return num + 1
            num += 1
        return num

    def checkRight(r,c):
        num = 0
        for i in range(c + 1, COL):
            if inp[r][i] >= inp[r][c]:
                return num + 1
            num += 1
        return num
    
    def checkLeft(r,c):
        num = 0
        for i in range(c - 1, -1, -1):
            if inp[r][i] >= inp[r][c]:
                return num + 1
            num += 1
        return num

    res = 0
    for r in range(1,ROW - 1):
        for c in range(1, COL - 1):
            tmp = checkBottom(r,c) * checkTop(r,c) * checkLeft(r,c) * checkRight(r,c)
            res = max(res, tmp)

    print(res)


if __name__ == "__main__":
    main()

#1776 234416