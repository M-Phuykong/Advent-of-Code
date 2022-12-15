
def main():

    input_file = "Day10/input.txt"

    with open(input_file) as f:
        lines = list(map(str.strip,f.readlines()))

    res = []
    threshold = [20,60,100,140,180,220]
    cycle = 0
    register = 1

    for line in lines:
        
        # if threshold and cycle >= threshold[0]:
        #     res.append(register * threshold[0])
        #     threshold.pop(0)

        if 'noop' in line:
            cycle += 1
            
            if  register <= cycle % 40 < register + 3:
                res.append("#")
            else:
                res.append(".") 

            if (cycle % 40 == 0):
                res.append("\n")  

        else:
            _, val = line.split()
            val = int(val)
            
            for _ in range(2):
                cycle += 1

                if  register <= cycle % 40 < register + 3:
                    res.append("#")
                else:
                    res.append(".") 
                
                if (cycle % 40 == 0):
                    res.append("\n")  

                # if threshold and cycle >= threshold[0]:
                #     res.append(register * threshold[0])
                #     threshold.pop(0)
            
            register += val

    # print(lines)
    print("".join(res))
if __name__ == "__main__":
    main()

