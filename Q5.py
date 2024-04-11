mark= float(input ("Your mark: "))

if mark <= 80:
    if mark < 25:
        print("F")
    elif 23 < mark < 45:
        print("E")
    elif 45 < mark < 50:
        print("D")
    elif 50 <mark <  60:
        print("C")
    else: 
        print("B")
else:
    print("A")