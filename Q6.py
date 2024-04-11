# A student will not be allowed to sit in exam if his/her attendance is less 
# than 75%.
# a. Take following input from user
# i. Number of classes held
# ii. Number of classes attended.
# b. Print percentage of class attended
# c. Print Is student is allowed to sit in exam or not.

Classes= int(input("Number of classes held: "))
Classes_attended= int(input ("Number of classes attended: "))
if Classes <= 0:
    print (None, "Invalid input: Classes held cannot be zero or negative.")
attendance_percentage = (Classes_attended / Classes) * 100
print(attendance_percentage)

if attendance_percentage <= 75:
    print( "A student will not be allowed to sit in exam")
else:
    print( "A student will be allowed to sit in exam")