val_txt = input("enter : ")
val = int(val_txt)
if(val>1):
    for i in range(2,val):
        if (val%i == 0):
            print("Not a prime number")
            break
    else:
        print("Prime")
else:
    print("nope")
