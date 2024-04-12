input = [1,2,3,4]
a = []
def add(input):
    for i in range (1, len(input)):
        for j in range(1, len(input)):
            a.append(j)
            print(j)
add(input)