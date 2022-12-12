#Chandler's coffee shop barrista
#Mimic a real life barrista for a coffee shop simulation

print("Hello, welcome to Chandler's Coffee Shop \n")

name = (input("What is your name? \n"))

if name == "Jenny" or name == "Dr Doom":
    evil_status = input("Are you evil?\n").lower()
    good_deeds = int(input("How many good deeds have you done today?\n"))
    if evil_status == "no":
        print("Brilliant, We are glad you are now good " + name + "\n")
    elif evil_status == "yes" and good_deeds >= 4:
        print("Well at least your trying to be good " + name + "\n")
    elif evil_status == "yes" and good_deeds < 4:  
        print("You are not welcome here " + name + "!!! Get out and don't come back!!!")
        exit()
        
if name == "Chandler":
        Chandler_Coffee = (input("Hey Chandler, Latte again for you? \n")).lower()
        if Chandler_Coffee == "yes":
            print("Great choice, a man of routine \n")
            print("It will be ready in T-minus 10 seconds \n")
            import time
            time.sleep(5)
            print("Look at that, ready in 5 seconds \n")
            print("We're efficient here Boss! \n")
            print("Have a marvellous day " + name + " see you next time")
            exit()
        elif Chandler_Coffee != "yes":
            print("What would you like to order from our menu?"+ "\n")
        else:
            print("Hello " + name + ", thank you for coming in today \n")
            print("What would you like to order from our menu?"+ "\n")
    
menu = "Espresso, Black Coffee, Macchiato, Latte, Cappucino, Mochachino, Flat White, Tea"
print("You can choose from: \n" + menu)
import time
time.sleep(3)

order = input().lower()
while order != "espresso" and order != "black coffee" and order != "macchiato" and order != "latte" and order != "cappucino" and order != "mochachino" and order != "flat white" and order != "tea":
    print("Sorry, we don't have that here.\nBut our menu does have the following:\n" + menu )
    order = input().lower()
if order == "espresso":
    price = 2.60
elif order == "black Coffee":
    price = 3
elif order == "macchiato":
    price = 3.30
elif order == "latte":
    price = 3.70
elif order == "cappucino":
    price = 3
elif order == "mochachino":
    price = 3.90
elif order == "flat white":
    price = 3.50
elif order == "tea":
    price = 2.40


quantity = input("\nHow many " + order + "'s would you like?\n")

#Price not working, cant find?
total = price * int(quantity)
format_total = "{:.2f}".format(total)

import time
time.sleep(3)
print("Fantastic " + name + ", Your total today is: $" + str(format_total) + "\n")


payment = (input("Are you paying by cash or card today? \n")).lower()

if payment == "cash":
    import time
    time.sleep(3)
    print("Thank you, let me just get your change \n")
elif payment == "card":
    print("Brilliant, just put your card into the machine for me please")
    import time
    time.sleep(3)
    print("And now type in your pin")
    i=1
    while i<=5:
        time.sleep(2)
        print("...")
        i=i+1
    print("Yep, that's all gone through")

#WHILE LOOP to head back to cash/card option
#elif:
    #print("Sorry, we only accept cash or card")

if int(quantity) != 1:   
    print("\nI will have your order of " + str(quantity) + " " + order + "'s ready shortly " + name + ".\n")
else:
    print("\nI will have " + order + " ready shortly " + name + ".\n")
    
import time
time.sleep(3)

if int(quantity) == 1:
    import time
    time.sleep(2)
    print("...\n")
    time.sleep(2)
    print(name + ", your " + order + " is ready")
elif int(quantity) <= 3:
    import time
    time.sleep(2)
    print("...\n")
    j=1
    while j<=4:
        time.sleep(2)
        print("...")
        j=j+1
    print("Been on holiday any where nice recently?\n")
    time.sleep(2)
    k=1
    while k<=3:
        time.sleep(2)
        print("...")
        k=k+1
    print(name + ", your " + quantity + " " + order + "'s are ready")
elif int(quantity) > 3:
    import time
    time.sleep(2)
    print("...\n")
    j=1
    while j<=4:
        time.sleep(2)
        print("...")
        j=j+1
    print("Can't believe the weather we've been having lately?\n")
    k=1
    while k<=4:
        time.sleep(2)
        print("...")
        k=k+1
    print("Been on holiday any where nice recently?\n")
    l=1
    while l<=2:
        time.sleep(2)
        print("...")
        l=l+1
    print(name + ", your " + quantity + " " + order + "'s are ready")

import time
time.sleep(2)

print("Have a marvellous day " + name + " see you next time")
exit()

