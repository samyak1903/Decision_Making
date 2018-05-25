#Q.3- Take the input age of 3 people and determine oldest and youngest among them.
a1=int(input("Enter age of first person"))
a2=int(input("Enter age of second person"))
a3=int(input("Enter age of third person"))
if a1>=a2 and a1>=a3:
    oldest="first"
    if a2<=a3:
        youngest="second"
    else:
        youngest="third"

if a2>=a1 and a2>=a3:
    oldest="second"
    if a1<=a3:
        youngest="first"
    else:
        youngest="third"

if a3>=a2 and a3>=a1:
    oldest="third"
    if a2<=a1:
        youngest="second"
    else:
        youngest="first"

print("Youngest person is {} and oldest person is {}".format(youngest,oldest))
