input = [1,2,3]
a = []
def con(input):
    for i in range (1, len(input)):
        for j in range(1, len(input)):
            if j == 2:
                continue 
            print(j)
con(input)