'''Q.4- Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service. 

1. if employee is female, then she will work only in urban areas.
2. if employee is a male and age is in between 20 to 40 then he may work in anywhere
3. if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
4. And any other input of age should print "ERROR".
Q.5- A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user. 
'''
age=int(input("Enter the age of employee: "))
sex=input("Gender: M or F: ")
status=input("Marital status: Y/N: ")
if sex.upper()=='F':
    print("Employee will work only in urban areas ")
if sex.upper()=='M':
    if age>=20 and age<=40:
        print("Emoployee can work anywhere")
    elif age>=40 and age<=60:
        print("Employee will work only in urban areas")
    else:
        print("ERROR")

