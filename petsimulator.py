# pet dictionary
pet = {"name": "", "type": "", "age": 0, "hunger": 0, "toys": []}

# pet toys data object
petToys = {"cat": ["scratching post", "toy mouse", "ball of yarn"], "dog": ["chew toy", "stick", "frisbee"], "fish": ["undersea castle", "fake coral", "buried treasure"], "dragon": ["castle", "fireball", "princess"] }
# Prompt for different options for pet types
def initPet():
    petType = ""
    # get the input of what type of pet this is


    petOptions = list(petToys.keys())

    # validate the input
    while petType not in petOptions:
        print("Please input a type of pet from the following options: ")
        for option in petOptions:
            print(option)
        petType = input("Please input one of the pets: ")

    # write in the pet type into the database
    pet["type"] = petType
    # name our pet
    pet["name"] = input("What would you like to name your " + pet["type"] + "? ")



    #write to our pet dictionary to store



# Print menu
def printMenu(menuOptions):
    optionKeys = list(menuOptions.keys())

    print("Here are your options: ")
    print("---------")
    for key in optionKeys:
        print(key + ":\t" + menuOptions[key]["text"])
# Play with our toys
def playToys():
    print(pet["name"] + " had a wonderful time playing with the toys!")
# Get new toys
def getToys():
    print("Yay! Let's get some new toys!")
    toyOptions = petToys[pet["type"]]

    # Specific toy number to select from the list
    toyNum = -1

    # get a vlid toy to input
    while toyNum < 0 or toyNum > len(toyOptions) - 1:
        for i in range(len(toyOptions)):
            print(str(i) + ": " + toyOptions[i])
        toyNum = int(input("Input the number of the toy you would like: "))

    # get the selected toy option from our list
    chosenToy = toyOptions[toyNum]
    pet["toys"].append(chosenToy)
    print("Nice! You selected the " + chosenToy + "!")
# Quit to game
def quitSimulator():
    print("Quit the simulator. Thanks for playing!")

# Feed our pet
def feedPet():
    # handle negative age cases
    newHunger = pet["hunger"] - 20
    if newHunger < 0:
        newHunger = 0
    pet["hunger"] -= 20
    print("Fed your pet, decreasing hunger by 10")

# print stats about pet
def printStats():
    print("Your " + pet["type"] + " " + pet["name"] + " is doing great!")
    print("Your pet currently has: " + str(len(pet["toys"])) + " toys, which are: ")
    for toy in pet["toys"]:
        print(toy)
    print("Your pet is currently at hunger of " + str(pet["hunger"]) + " of a max of 100.")
    print("Your pet is " + str(pet["age"]) + " days old.")

# Main game loop
def main():
    # initialize pet


    # print menu
    initPet()

    # menu options for printing and access

    menuOptions = {"Q": { "function": quitSimulator, "text": "Quit the game"}, "F": { "function": feedPet, "text": "Feed " + pet["name"] }, "P": { "function": playToys, "text": "Play with " + pet["name"] }, "G": { "function": getToys, "text": "Get new toys for " + pet["name"] + "!" } }


    keepPlaying = True
    while keepPlaying:
        # Print the menu
        menuSelection = ""

        # get input
        # validate the input.
        while menuSelection not in menuOptions.keys():
            printMenu(menuOptions)
            menuSelection = input("Which of these meny options would you like to use? ").upper()
        # Quit game when user puts in Q
        if menuSelection == "Q":
            keepPlaying = False

        # invoke the function corresponding to the selected menu option
        menuOptions[menuSelection]["function"]()

        # increase pet hunger
        pet["hunger"] += 10
        pet["age"] += 1

        printStats()
        # print out an extra line between options
        print()


main()