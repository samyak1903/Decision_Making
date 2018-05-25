#Q.1- Take an input year from user and decide whether it is a leap year or not.
n=int(input("Enter the year as yyyy:"))
if n%400==0:
    print("Leap Year")
elif n%4==0 and n%100!=0:
    print("Leap Year")
else:
    print("Not a leap year")
