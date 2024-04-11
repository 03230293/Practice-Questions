num1=(input(" One number: "))
num2=(input(" two number: "))
num3=(input(" three number: "))

if num1 > num2 and num1 > num3:
    print (num1, "is the greatest number.")
elif num2 > num1 and num2 > num3:
    print(num2, " is the greatest number.")
elif num3 > num1 and num3 > num2:
    print( num3, " is the greatest number.")
else:
    print("All three numbers are equal.")