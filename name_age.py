name = input("what's your name : ")
print("nice name",name)
while True:
    try:
        age = int(input("Now tell your age : "))
        print("Wow!!! very young")
        break
    except:
        print("Bruh!!! enter in numbers...try again")
    
print("name is", name, "and age is ", age)
