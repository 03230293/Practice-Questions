# . printed price between 500 and 1000, allow 5% discount
# b. printed price between 1000 and 5000, allow 10% discount
# c. printed price between 5000 and 10000, allow 15% discount
# d. printed price more than 10000, allow 20% discount

printed_prices= int(input("Printed price: "))
if 500 < printed_prices < 10000:
    if 500 < printed_prices < 1000:
        print("Allow 5% discount")
    elif 1000 < printed_prices < 5000:
        print("Allow 10% discount")
    else: 
        print("Allow 15% discount")
    
else:
    print("printed price more than 10000, allow 20% discount")