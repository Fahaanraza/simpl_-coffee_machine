print("""                      .-.       .-.                                                            ___                                 
                    /    \    /    \                                                         (   )       .-.                      
  .--.      .--.    | .`. ;   | .`. ;    .--.     .--.      ___ .-. .-.     .---.    .--.     | | .-.   ( __)  ___ .-.     .--.   
 /    \    /    \   | |(___)  | |(___)  /    \   /    \    (   )   '   \   / .-, \  /    \    | |/   \  (''") (   )   \   /    \  
|  .-. ;  |  .-. ;  | |_      | |_     |  .-. ; |  .-. ;    |  .-.  .-. ; (__) ; | |  .-. ;   |  .-. .   | |   |  .-. .  |  .-. ; 
|  |(___) | |  | | (   __)   (   __)   |  | | | |  | | |    | |  | |  | |   .'`  | |  |(___)  | |  | |   | |   | |  | |  |  | | | 
|  |      | |  | |  | |       | |      |  |/  | |  |/  |    | |  | |  | |  / .'| | |  |       | |  | |   | |   | |  | |  |  |/  | 
|  | ___  | |  | |  | |       | |      |  ' _.' |  ' _.'    | |  | |  | | | /  | | |  | ___   | |  | |   | |   | |  | |  |  ' _.' 
|  '(   ) | '  | |  | |       | |      |  .'.-. |  .'.-.    | |  | |  | | ; |  ; | |  '(   )  | |  | |   | |   | |  | |  |  .'.-. 
'  `-' |  '  `-' /  | |       | |      '  `-' / '  `-' /    | |  | |  | | ' `-'  | '  `-' |   | |  | |   | |   | |  | |  '  `-' / 
 `.__,'    `.__.'  (___)     (___)      `.__.'   `.__.'    (___)(___)(___)`.__.'_.  `.__,'   (___)(___) (___) (___)(___)  `.__.'  
                                                                                                                                  
                                                                                                                                   """)
machine = {"espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
           "cappucino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0},
           "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5}
           }


resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0}
penny = 0.01
nickel = 0.05
dime = 0.10
quarter = 0.25
off = False


def cost():
    global nickell, dimee, pennyy, quarterr, total
    total = 0
    pennyy = 0
    nickell = 0
    dimee = 0
    quarterr = 0
    print("insert the coins please!!")
    pennyy = float(input("how many penny: "))*penny
    nickell = float(input("how many nickel: "))*nickel
    dimee = float(input("how many dime: "))*dime
    quarterr = float(input("how many quarter: "))*quarter
    total = pennyy+nickell+dimee+quarterr
    print("money received:$", total)


def oorder():
    order = input("What would you like to have? Latte, Cappucino, Espresso?  ")
    if(order == "latte"):
        cost()
        a = (machine["latte"])
        b = a["ingredients"]
        if((resources["water"]) < 0):
            print("sorry water is over sir!!")
        elif((resources["milk"]) < 0):
            print("sorry milk is over sir!!")
        elif((resources["coffee"]) < 0):
            print("sorry coffee is over sir!!")
        elif (total <= a["cost"]):
            print("money is less bruh")
            print("here is ur refund: $", total)
        elif(total >= a["cost"]):
            resources["money"] += a["cost"]
            resources["water"] -= b["water"]
            resources["coffee"] -= b["coffee"]
            print("$", total-a["cost"], "is your change sir/madam")
            print("here is you latte!! ENjoy sir/madam")

    elif(order == "cappucino"):
        cost()
        a = (machine["cappucino"])
        b = a["ingredients"]
        if(resources["water"] < 0):
            print("sorry water is over sir!!")
        elif(resources["milk"] < 0):
            print("sorry milk is over sir!!")
        elif(resources["coffee"] < 0):
            print("sorry coffee is over sir!!")
        elif (total <= a["cost"]):
            print("money is less bruh")
            print("here is ur refund: $", total)
        elif(total >= a["cost"]):
            resources["money"] += a["cost"]
            resources["water"] -= b["water"]
            resources["milk"] -= b["milk"]
            resources["coffee"] -= b["coffee"]
            print("$", total-a["cost"], "is your change sir/madam")
            print("here is you cappucino!! ENjoy sir/madam")
    elif(order == "espresso"):
        cost()
        a = (machine["espresso"])
        b = a["ingredients"]
        if(resources["water"] < 0):
            print("sorry water is over sir!!")
        elif(resources["milk"] < 0):
            print("sorry milk is over sir!!")
        elif(resources["coffee"] < 0):
            print("sorry coffee is over sir!!")
        elif (total <= a["cost"]):
            print("money is less bruh")
            print("here is ur refund: $", total)
        elif(total >= a["cost"]):
            resources["money"] += a["cost"]
            resources["water"] -= b["water"]
            resources["milk"] -= b["milk"]
            resources["coffee"] -= b["coffee"]
            print("$", total-a["cost"], "is your change sir/madam")
            print("here is you espresso!! ENjoy sir/madam")

    elif(order == "report"):
        global off
        print("water: ", resources["water"], "ml")
        print("milk: ", resources["milk"], "ml")
        print("coffee: ", resources["coffee"], "ml")
        print("money:$ ", resources["money"])
    elif(order == "off"):
        off = True


while off == False:
    oorder()
