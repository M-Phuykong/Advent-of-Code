import pprint

def main():
    
    input_file = "Day9/input.txt"

    with open(input_file) as f:
        lines = list(map(str.strip,f.readlines()))

    print(lines)
    visit = set()

if __name__ == "__main__":
    main()
