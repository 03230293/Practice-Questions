salary= float(input("Enter your salary: "))

if salary <= 50000:
    if salary < 10000:
        print(" 5% increment")
    elif  10000 < salary < 20000:
        ("10 % increment")

    elif 20000 < salary < 50000 :
        print("15 % increment")
else:
    print("salary more than 50,000, 20 % increment")