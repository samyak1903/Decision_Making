#Q.5- A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user. 
quant=int(input("Input the quantity of the item: "))
cost=float(quant*100)
print("Initial cost of {0} items={1}".format(quant,cost))
if cost>1000:
    print("Giving 10% discount")
    print("Discount=%f" %(cost*0.1))
    cost=cost*0.9
print("Total cost={}".format(cost))

