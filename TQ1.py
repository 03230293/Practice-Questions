n=3
def sum_of_squares(n):
    total = 0
    for i in range(1, n+1):
        total += i**2
    print (total)
sum_of_squares(n)