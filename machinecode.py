#predefiend values
water = 400
milk = 540
coffee_beans = 120
disposable_cups = 9
money = 550

while True:
    action = input("Write action (buy, fill, take, remaining, exit):").strip().lower()

    if action == 'buy':

        type_coff = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:").strip()

        if type_coff == "back":
            continue

        if type_coff == '1':

            if (water >= 250) & (coffee_beans >= 16) & (disposable_cups >= 1):
                water = water - 250
                coffee_beans = coffee_beans - 16
                money = money + 4
                disposable_cups = disposable_cups - 1
                print("I have enough resources, making you a coffee!")

            elif water < 250:
                print("Sorry, not enough water!")
            elif coffee_beans < 16:
                print("Sorry, not enough coffee beans!")
            elif disposable_cups < 1:
                print("Sorry, not enough disposable cups!")


        elif type_coff == '2':

            if (water >= 350) & (coffee_beans >= 75) & (disposable_cups >= 1) & (milk >= 75):
                water = water - 350
                milk = milk - 75
                coffee_beans = coffee_beans - 20
                money = money + 7
                disposable_cups = disposable_cups - 1
                print("I have enough resources, making you a coffee!")

            elif water < 350:
                print("Sorry, not enough water!")
            elif milk < 75:
                print("Sorry, not enough milk!")
            elif coffee_beans < 75:
                print("Sorry, not enough coffee beans!")
            elif disposable_cups < 1:
                print("Sorry, not enough disposable cups!")



        elif type_coff == '3':

            if (water >= 200) & (coffee_beans >= 12) & (disposable_cups >= 1) & (milk >= 100):
                water = water - 200
                milk = milk - 100
                coffee_beans = coffee_beans - 12
                money = money + 6
                disposable_cups = disposable_cups - 1
                print("I have enough resources, making you a coffee!")

            elif water < 200:
                print("Sorry, not enough water!")
            elif milk < 100:
                print("Sorry, not enough milk!")
            elif coffee_beans < 12:
                print("Sorry, not enough coffee beans!")
            elif disposable_cups < 1:
                print("Sorry, not enough disposable cups!")

    if action == 'fill':
        add_water = int(input("Write how many ml of water do you want to add:"))
        add_milk = int(input("Write how many ml of milk do you want to add:"))
        add_coffee = int(input("Write how many grams of coffee beans do you want to add:"))
        add_disposable = int(input("Write how many disposable cups of coffee do you want to add:"))

        water += add_water
        milk += add_milk
        coffee_beans += add_coffee
        disposable_cups += add_disposable

    if action == 'take':
        print("I gave you ${}".format(money))
        money = 0

    if action == 'remaining':
        print("The coffee machine has:")
        print(water, "of water")
        print(milk, "of milk")
        print(coffee_beans, "of coffee beans")
        print(disposable_cups, "of disposable cups")
        print("${} of money".format(money))

    if action == 'exit':
        break
