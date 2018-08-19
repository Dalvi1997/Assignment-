mrp=int(input("Enter mrp"))
offerno=int(input("Enter offer number"))
if(offerno ==1):
    discount=mrp * 0.25
    print(" with mrp {} offerno{} the final value is {}".format(mrp,offerno,discount))
elif(offerno ==2):
    discount=mrp*0.4
    print("with mrp {} offerno {}the final value is {}".format(mrp,offerno,discount))
elif(offerno ==3):
    discount=mrp*0.6
    print(" with mrp{} offer number{} the final value is {}".format(mrp,offerno,discount))
else:
    print(" no discount")
