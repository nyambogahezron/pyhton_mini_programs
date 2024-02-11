name = input("Type you name: ")
print("Welcome", name, "to this adventure!")
option = input("You are on a dirt road, it as come to an end and you can go left or right. Which way would you like to go? ").lower()


if option == "left":
    option = input("You come to a river,you can walk around it or swim across? Type walk to walk around and swim to swim across: ")
    if option == "swim":
        print("You swan across and eaten by an alligator.")
    elif option == "walk":
        print("You walked for many miles and ran out of water and you lost")
    else:
        print("Not a valid option. You lose.")

elif option == "right":
    option = input("You come to a bridge, its looks wobbly, do you want to cross it or head back (cross/back)? ")

    if option == "back":
        print("You went back and lost.")
    elif option == "cross":
            option = input("You meet a stranger. Do you talk to them(yes/no). ")
            if option == "yes":
                print("You talk to the strangers and give you gold. You WIN!")
            elif option == "no":
                print("you ignore the strangers and they are offended and you lose")
            else:
                print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")



else:
    print("Not a valid option. You lose.")


print("Thanks for trying", name)



