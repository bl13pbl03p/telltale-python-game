# Imports
# time is a module to handle tasks related to the time.
import time
# The sys module is a set of functions which provide crucial information about how your Python script is interacting with the host system.  # noqa: E501
import sys

q1 = input("What is your name: ")
print("Welcome", q1)

q2 = input("Do you prefer white rice or spaghetti? ")
if q2 == "white rice":
    print("You have quite the taste my young man.")
# isdigit() checks if the user's input is a number
elif q2.isdigit():
    print("So you eat numbers? Alright then.")
else:
    print("You are not taking this 'rip off' telltale games seriously aren't you?")  # noqa: E501

# As an user you can only continue to the next question if your answer complies within the asked requirements  # noqa: E501
while True:
    q3 = input("What is your lucky number? ")
    try:
        # Here I converted the input to an int
        q3 = int(q3)
        # If the number is higher 100 or higher the user won't proceed
        if q3 >= 100:
            print("Pick a number below the 100")
        # If the user's input is under the 100 he'll pass
        else:
            hp = q3
            break
    # When I filled in a string value in the input I got back the error "ValueError" and the code stopped running.  # noqa: E501
    # Instead I made a workaround ensured that the user can still try to fill in a correct value  # noqa: E501
    except ValueError:
        print("No letters, numbers please!")

# This is a function that checks the hp of the user.
def hp_check():
    if hp < 1:
        print("\nUuuuhm you are out of health points", q1, "... Unfortunately peanut butter :(")  # noqa: E501
        game_over = "Thank you for playing my game it has been a honour."
        # This loop prints the content of the variable game_over in a 'typewriting' output.  # noqa: E501
        for word in game_over:
            # Changes the end character of a print to an empty string.
            print(word, end='')
            # Causes to print instantly, because normally it's buffered.
            sys.stdout.flush()
            # This function pauses Python programs.
            time.sleep(0.17)

        print("\nYou ended with,", hp, "health points.")
        # Function to end the Python script.
        quit()

# Here, my game begins.
print(
    """
    +=====================================================================================================+
     Great""", q1, """that means that you'll receive""", q3, """hp (health points) in this adventure.
     The adventure adapts to the choices you make.
     The story is tailored by how you play.

     Good luck.
    +=====================================================================================================+
    """)

# Here I made a while loop.
while True:
    q4 = input("\nDo you prefer walking or cycling: ")
    # .lower() causes that it's irrelevant whether the input is filled in capitals or not.  # noqa: E501
    if q4.lower() == "walking":
        answer = input("\nOh no, you encountered a wild brown feathered goose. \n\nChoices: \na)Kill goose. \nb)Run away! \nI choose ")  # noqa: E501
        # Checks if the users input is, longer than 2 characters, an empty input or a number.  # noqa: E501
        if answer == "a" or (len(answer)) >= 2 or None or answer.isdigit():
            hp -= 10
            print("You slaughtered a goose, are you mad? You have", hp, "hp left.")  # noqa: E501
            # Here I'm calling my function to check if the user has enough HP
            hp_check()
            break
        else:
            print("You managed to get away just yet, now you are in a local Lidl.\nSo you still have", hp, "hp left!")  # noqa: E501
            break
    elif q4.lower() == "cycling":
        answer = input("\nA stranger asks you if you could help him with finding his dog. \nChoose: \na)You'll help. \nb)You steal his 1000 coins. \nc)You politely decline his request \nI choose ")  # noqa: E501
        if answer == "a":
            hp += 10
            print("You managed to find his little puppy!! You will receive 10 hp.")  # noqa: E501
            break
        elif answer == "b" or None or (len(answer)) >= 2 or answer.isdigit():
            hp -= 30
            print("Coins won't help you in this game, the stranger shoots in your right knee.\nYou know have", hp, "hp left.")  # noqa: E501
            hp_check()
            break
        else:
            print("The stranger starts crying and you walk away like nothing happened.")  # noqa: E501
            break
    else:
        print("What do you prefer??")


if hp > 50:
    answer = input("\nIt's starting to get dark and you suddenly hear gunshots nearby. \nChoices: \na)Look for shelter in the most nearby village. \nb)Keep on walking towards the gunshots. \nI choose ")  # noqa: E501
    if answer == "b" or (len(answer)) >= 2 or None or answer.isdigit():
        hp -= 30
        print("Someone attacks you from behind and you lose consciousness.")
        hp_check()
    else:
        print("You managed to find an abandoned factory.")
else:
    answer = input("\nIt's starting to get dark and you suddenly hear fireworks nearby. \nChoose: \na)You are going towards the fireworks. \nb)Search for a hotel to spend the night \nc)Eat a banana because you are hungry \nI choose ")  # noqa: E501
    if answer == "a" or None or (len(answer)) >= 2 or answer.isdigit():
        hp -= 30
        print("Someone attacks you from behind and you lose consciousness.")
        hp_check()
    elif answer == "b":
        print("You checked in in hotel Les Deux Baguettes.\nYou still have", hp, "hp left.")  # noqa: E501
    else:
        hp += 1
        print("The banana gave you 1 hp and you are spending the night on a bench in the park.")  # noqa: E501

print("\nWow, I'm impressed that you have come so far. Let's see how long you'll last.")  # noqa: E501


if hp > 30:
    answer = input("\nSlowly, you wake up and discover that your right thumb has been chopped off.\nChoices: \na)Shout for help \nb)Take the bus to a local pharmacy \nI choose ")  # noqa: E501
    if answer == "b" or (len(answer)) >= 2 or None or answer.isdigit():
        hp -= 40
        print("You slipped over a peeled banana and got traumatized. You have", hp, "hp left.")  # noqa: E501
        hp_check()
    else:
        hp += 39
        print("A random cyber security student offers you a bowl of fried rice and you accept it.\nThis delicious meal gives you 39 hp!")  # noqa: E501
else:
    answer = input("\nAs you wake up, you see a breakfast meal laying in front you. \nChoose: \na)Eat. \nb)You pack the meal and store it for later \nc)Restart game. \nI choose ")  # noqa: E501
    if answer == "a" or None or (len(answer)) >= 2 or answer.isdigit():
        hp -= 30
        print("You choke in a cheese croissant, what s shame. Now you are 30 hp lighter.")  # noqa: E501
    elif answer == "b":
        print("That's smart, you are smart.")
    else:
        hp -= 27
        print("Nice try potato head, but that's not an option. You lose 27 hp.")  # noqa: E501
        hp_check()


if hp > 60:
    game_over = "\nThank you for playing my game it has been a honour. You are the best!"  # noqa: E501
    print("\nYou ended with a total of", hp, "health points.")

    for word in game_over:
        print(word, end='')
        sys.stdout.flush()
        time.sleep(0.13)
else:
    game_over = "\nThank you for playing my game it has been a honour. You did well!"  # noqa: E501
    print("\nYou ended with,", hp, "health points.")

    for word in game_over:
        print(word, end='')
        sys.stdout.flush()
        time.sleep(0.13)


# DISCLAIMER
# Some comments I only wrote once, otherwise you'll see the same comments all over again.  # noqa: E501
